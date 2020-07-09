from django.shortcuts import render
from django.http import HttpResponse,JsonResponse



#=====================================================
#--------------    Webpage      ---------------------
#======================================================


#----------------------------------------
#-- Home PAGE --- url - baseurl/ --------
#----------------------------------------
def home(request):
    return render(request ,"ApiHandler/home.html")

#----------------------------------------


