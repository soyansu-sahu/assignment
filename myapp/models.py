from django.db import models



# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key = True,unique=True,null=False, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique = True)
    mobile_no = models.CharField(max_length=20,null=False, blank=False,unique=True)

    def __str__(self):
        return self.first_name



class Customer(models.Model):
    profile_number = models.IntegerField(primary_key=True)
    customer = models.OneToOneField(User,on_delete = models.CASCADE)
   

    def __str__(self):
        return f'{self.customer}'








