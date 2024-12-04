from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class District(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, related_name='districts', on_delete=models.CASCADE)

    def __str__(self):   
        return self.name
    
class Post(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    language = models.CharField(max_length=50)
    state = models.ForeignKey(State,related_name='posts', on_delete=models.CASCADE)
    district = models.ForeignKey(District,related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name    
    