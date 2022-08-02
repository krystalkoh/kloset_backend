from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, email, given_name, other_name, password=None):
        if not email:
            raise ValueError('User must have a valid email.')

        user = self.model(
            email=self.normalize_email(email), #normalize_email makes email address all small
            given_name=given_name,
            other_name=other_name,
        )
        user.set_password(password) #set_password encrypts the password automaticlaly
        user.save(using=self._db)

        return user

    def create_superuser(self, email, given_name, other_name, password):
        user = self.create_user(
            email=email,
            given_name=given_name,
            other_name=other_name,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)\

        return user

##creating actual table now. each line is a column in the account table
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    given_name = models.CharField(max_length=30)
    other_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    #the following 4 is required... cannot change
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()
    ##when creating a new user
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['given_name', 'other_name']
    ##don't need fill in other fields

    def __str__(self):
        return f'{self.given_name} {self.other_name}'
    #has_perm=have permissions...overwriting django permissions. This checks whether you're an admin anot
    def has_perm(self, perm, obj=None):
        return self.is_admin
    #which views does the user have permission to
    def has_module_perms(self, app_label):
        return True
