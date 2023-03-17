from django.db import models
from django.db import models
# from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
# from django.db import transaction
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_owner = models.BooleanField('Is owner', default=False)
    is_public = models.BooleanField('Is public', default=False)

     
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    # fullname=models.CharField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    user_email=models.EmailField(max_length=100,blank=True,null=True)
    profile_pic=CloudinaryField('image')
    biography=models.TextField(blank=True,null=True)
    contact_number=models.CharField(max_length=200)
    location=models.CharField(max_length=200)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def profile_update(self,id,profile):
        updated_profile=Profile.objects.filter(id=id).update(profile)
        return updated_profile

    def __str__(self):
        return str(self.username)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

        post_save.connect(Profile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile
 
    
class Ambulance(models.Model):
    image=CloudinaryField('image', null=True)
    ambulance_properties = models.TextField(null=True)
    ambulance_name =models.CharField(max_length=50 , null=True)
    current_location = models.CharField(max_length=100, null=True)
    availability= models.CharField(max_length=10)
    hire_price= models.IntegerField(default=0)
    accident_pay_rate = models.FloatField(default=0.0)
    events_pay_rate= models.IntegerField(default=0)
    patient_transport_pay_rate= models.IntegerField(default=0)
    basic_life_support_pay_rate= models.IntegerField(default=0)
    driver_name = models.CharField(max_length=50 , null=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone_number = models.IntegerField(null=True)
    
    
    def save_ambulance(self):
        self.save()

    def update_ambulance(self):
        self.update()

    def delete_ambulance(self):
        self.delete()
        
    @classmethod
    def find_ambulance(cls,ambulance_id):
        new_ambulance = cls.objects.filter(ambulance_id=ambulance_id)
        return new_ambulance

    def __str__(self):
        return self.ambulance_name
    
    
class Owner_post(models.Model):
    ambulance_name=models.CharField(max_length=100,null=True,blank=True)
    ambulance_image=CloudinaryField('ambulance_image',blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post",null=True,blank=True)
    describe=models.TextField(null=False)
    posted_at=models.DateTimeField(auto_now_add=True,)
    pay_rate=models.CharField(max_length=100,null=True,blank=True)

    def save_owner_post(self):
        self.save()

    def delete_owner_post(self):
        self.delete()

    def update_owner_post(self,id,owner_post):
        updated_post=Owner_post.objects.filter(id=id).update(owner_post)
        return updated_post


    def __str__(self):
        return self.ambulance_name
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=15)
    address = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    service=models.CharField(max_length=40, null=True)
    ambulance_id = models.ForeignKey(Ambulance, on_delete=models.CASCADE, null=True)
    ambulance_name=models.CharField(max_length=100,null=True,blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def save_order(self):
        self.save()

    def delete_order(self):
        self.delete()

    def update_order(self,id,order):
        updated_order=Order.objects.filter(id=id).update(order)
        return updated_order
    
    @classmethod
    def get_orders(cls,id):
        orders = Order.objects.filter(ambulance_id__pk = id)
        return orders


    def __str__(self):
        return self.ambulance_name
    
class Customer(models.Model):
    customer_name=models.CharField(max_length=50)
    customer_id =models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    
class Feedback(models.Model):
    user_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=70, null=True, blank=True)
    content=models.TextField(null=True)
    rating = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ambulance_id =models.ForeignKey(Ambulance, on_delete=models.CASCADE, null=True)
    