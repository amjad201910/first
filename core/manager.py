
from django.contrib.auth.base_user import BaseUserManager

from django.core.exceptions import ValidationError

from rest_framework.exceptions import ValidationError as DRFValidationError
import json
import phonenumbers
from phonenumbers import geocoder

class UserManager(BaseUserManager):
    use_in_migrations = True




    def create(self, password=None, **extra_fields):
        parsed_number = phonenumbers.parse(extra_fields['phone'])
        extra_fields['country'] = geocoder.country_name_for_number(parsed_number,"en")




   

 
        user = self.model(**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, **extra_fields):
        parsed_number = phonenumbers.parse(extra_fields['phone'])
        extra_fields['country'] = geocoder.country_name_for_number(parsed_number,"en")


        user = self.model(**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.active = True
        user.group='admin'
        user.save(using=self._db)

        return user



    def update(self, user_id, **kwargs):
            print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPpppp")

           


            user = self.get(id=user_id)

            for attr, value in kwargs.items():
                setattr(user, attr, value)
            user.set_password(kwargs['password'])

            user.save(using=self._db)

            return user
