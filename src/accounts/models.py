from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'user_type'
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'
        ordering = ['name']
        
class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True)
    user_type = models.ForeignKey(UserType)
    
    primary_phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    business = models.TextField(null=True, blank=True)
    
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return ('%s' '%s') %(self.user.username , self.user.email)

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'