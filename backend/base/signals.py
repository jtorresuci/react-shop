# Gonna listen for a model to save and fire off action before it saves
from django.db.models.signals import pre_save
# Fire off action anytime a user model action is updated or created
from django.contrib.auth.models import *

# @param **kwargs: keyword arguments

def updateUser(sender, instance, **kwargs):
    print('Signal Triggered')
    # Duct tape fix can override user model but this works
    user = instance
    if user.email != '':
        user.username = user.email

# Before the user is saved fire off the updateUser function
pre_save.connect(updateUser, sender=User)
