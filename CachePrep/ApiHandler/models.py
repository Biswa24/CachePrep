from django.db import models
import os 

def question_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT /Questions/image/<filename>
    return 'Questions/image/{0}'.format(filename)


class Questions(models.Model):
    text = models.TextField('Question')
    img = models.FileField('Question Image',upload_to = question_image_path)
    tag = models.TextField('Question Tags')
    posted_on = models.DateField('Posted on',null=True,blank=True)


    def __str__(self):
        return self.text

    class Meta():
        verbose_name,verbose_name_plural = 'Questions','Questions'

