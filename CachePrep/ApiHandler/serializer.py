from rest_framework import serializers
from ApiHandler.models import Questions
from datetime import date


# ==========================================================================
# filter empty strings in tag 
def filtering_empty_string(tag):
    all_tags = list(tag.strip().split(','))
    filtered_tag = ' '.join(all_tags).split()
    ques_tag = ",".join(filtered_tag)

    return ques_tag


# ==========================================================================

class QuestionSerialzers(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'
    
    def create(self, validated_data):
        obj = Questions.objects.create(**validated_data,posted_on = date.today())
        obj.tag = filtering_empty_string(validated_data['tag'])
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        fields=instance._meta.fields
        for field in fields:
            field=field.name.split('.')[-1] 
            if field == 'tag':
                instance.tag = filtering_empty_string(validated_data.get(field, instance.tag))
            else:
                 exec("instance.%s = validated_data.get(field, instance.%s)"%(field,field))
        instance.posted_on = date.today()
        instance.save()
        return instance