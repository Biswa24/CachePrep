from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import operator
from functools import reduce
from django.db.models import Q


from ApiHandler.models import Questions
from ApiHandler.serializer import QuestionSerialzers,filtering_empty_string






#======================================================
#--------------    API'S      -------------------------
#=======================================================

#-- All Question --- url - baseurl/api/ --------
@api_view(['GET'])
def all_question(request):
    queryset = Questions.objects.all().order_by('-id')
    serializer = QuestionSerialzers(queryset,many=True)
    data = serializer.data

    return Response(data=data,status=status.HTTP_200_OK)



#-- Add Question --- url - baseurl/api/add/ --------
@api_view(['POST'])
def add_question(request):
    mode = request.method
    if mode == 'POST':
        
        serializer = QuestionSerialzers(data = request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
            
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


#----------------------------------------
#-- Update Question --- url - baseurl/api/update/<str:pk>/ --------
@api_view(['PUT','GET'])
def update_question(request,pk):
    try:
        ques_id = int(pk)
        ques_obj = Questions.objects.get(id=pk)
    except:
        data = {}
        data["Error"] = "id Invalid" 
        return Response(data=data,status=status.HTTP_404_NOT_FOUND)

    mode = request.method
    if mode == 'GET':

        serializer = QuestionSerialzers(ques_obj)
        return Response(serializer.data)

    if mode == 'PUT':

        serializer = QuestionSerialzers(instance = ques_obj,data = request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
        else:
            data = {}
            data["Error"] = "Invalid Data" 
            return Response(data=data,status=status.HTTP_409_CONFLICT)
        
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#----------------------------------------


#-- Tag Search --- url - baseurl/api/search/' --------
@api_view(['GET'])
def tag_search(request):
    mode = request.method
    if mode == 'GET':
        tags = request.GET.get('tag','')

        filtered_tags = filtering_empty_string(tag = tags)

        if filtered_tags == '':

            queryset = Questions.objects.all().order_by('-id')
            serializer = QuestionSerialzers(queryset,many=True)
            data = serializer.data

            return Response(data=data,status=status.HTTP_204_NO_CONTENT)
            
        else:
            tag_arr = list(filtered_tags.split(','))
            ques_data = Questions.objects.filter(reduce(operator.and_, (Q(tag__contains =i) for i in tag_arr)))
            serializer = QuestionSerialzers(ques_data,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_404_NOT_FOUND)