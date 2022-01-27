from django.db import models


# Django is based on MVT (Model View Template) architecture.
# Models are a key component of this architecture.
# Models are class based.
#
# Create your models here.

# Allows Practitioners to Sign In
class Practitioner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    email = models.CharField(max_length=255) 
    phone = models.CharField(max_length=255)

# Allows a Condition to be associated with a Practitoner, Single to Many, and to Treatments
class Conditions(models.Model):
    name_condition = models.CharField(max_length=255)

# Allows a Treatment to be associated with Conditions and Practitioners       
class Treatments(models.Model):
    medical = models.CharField(max_length=255)
    surgical = models.CharField(max_length=255)
    radiation = models.CharField(max_length=255)
    chemotherapy = models.CharField(max_length=255)
    other_alternative = models.CharField(max_length=255)
    palliative = models.CharField(max_length=255)
    clinical_trials = models.CharField(max_length=255)

# Allows Posts to be Utilized
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

