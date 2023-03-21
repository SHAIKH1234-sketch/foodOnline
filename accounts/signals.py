from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile
@receiver(post_save,sender=User)
def post_save_create_profile_reciver(sender,instance,created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('create the user profile')
    else:
        try:
            profile=UserProfile.objects.get(user=instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)
            print('profile was not created but i am created ome!!')
@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    print("user is being saved")
