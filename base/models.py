from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True,max_length=100) # balnk =true means , if we submit a form then in that case also its value can be empty
    participants=models.ManyToManyField(User,related_name='participants',blank=True) # we are adding a relative name as we have specified a connectio of host and participants with foriegn key above
    # also we have to submit a form without having to check something here, so that why we mentioned blank='True'
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True) # only take a timstamp when it is crated

    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True) # only take a timstamp when it is crated

    class Meta:
        ordering=['-updated','-created']
        
    def __str__(self):
        return self.body[0:50]
    