from django.db import models

# Create your models here.
#class Practitioner(models.Model):
#    first_name = models.CharField(max_length=255)
#   last_name = models.CharField(max_length=255)
#   occupation = models.CharField(max_length=255)
#   degree = models.CharField(max_length=255)
#   email = models.CharField(max_length=255) 
#   phone = models.CharField(max_length=255)

class Conditions(models.Model):
    name_condition = models.CharField(max_length=255)
      
class Treatments(models.Model):
    medical = models.BooleanField()
    surgical = models.BooleanField()
    radiation = models.BooleanField()
    chemotherapy = models.BooleanField()
    other_alternative = models.CharField(max_length=255)
    palliative = models.CharField(max_length=255)
    clinical_trials = models.BooleanField()

# class Tag(models.Model):
  #  tag_id = models.AutoField(primary_key=True)
   # name = models.CharField(max_length=255)

#class Post(models.Model):
 #   post_id = models.AutoField(primary_key=True)
  #  img_link = models.URLField()
   # title = models.CharField(max_length=255)
    #body = models.TextField()
    #tags = models.ManyToManyField(Tag)

#class Comment(models.Model):
 #   comment_id = models.AutoField(primary_key=True)
  #  comment = models.TextField()
   # post = models.ForeignKey(Post, on_delete=models.CASCADE)
