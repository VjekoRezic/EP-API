from django.db import models
from django.contrib.auth import models as auth_models
from workplace.models import Workplace
from work_center.models import WorkCenter
from datetime import date


class UserManager(auth_models.BaseUserManager):
    def create_user(self, first_name:str, last_name:str, father_name:str, date_of_birth:date, email:str, city:str, password:str=None, job_title:str=None, rfid_uid:str=None, workplace:Workplace=None, workcenter:WorkCenter=None)->"User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have first name")
        if not last_name:
            raise ValueError("User must have last name")
        if not father_name or not date_of_birth or not city:
            raise ValueError("User info missing")
       

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.father_name = father_name
        user.date_of_birth = date_of_birth
        user.city = city
        user.set_password(password)
        user.job_title = job_title
        user.rfid_uid = rfid_uid
        user.is_deleted = False
        user.workplace = workplace
        user.workcenter = workcenter
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name:str, last_name:str, father_name:str, date_of_birth:date, email:str, city:str, password:str, job_title:str=None, rfid_uid:str=None, workplace:Workplace=None, workcenter:WorkCenter=None)->"User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            date_of_birth=date_of_birth,
            email=email,
            city=city,
            password=password,
            job_title=job_title,
            rfid_uid=rfid_uid,
            workplace=workplace,
            workcenter=workcenter,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name='First name', max_length=255)
    last_name =  models.CharField(verbose_name='Last name', max_length=255)
    father_name = models.CharField(verbose_name="Fathers name", max_length=255)
    date_of_birth = models.DateField(verbose_name='Date of birth')
    email = models.EmailField(verbose_name="email", max_length=150, unique=True)
    city = models.CharField(verbose_name="city", max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', null=True)
    job_title = models.CharField(verbose_name="job title", max_length=255, null = True)
    rfid_uid = models.CharField(max_length=20, verbose_name='Card ID',unique=True, null=True)
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, verbose_name="workplace", null = True)
    workcenter = models.ForeignKey(WorkCenter, on_delete=models.CASCADE, verbose_name="work center", null=True) 
    username = None
    is_active=True
    last_login=None
    

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "father_name", "date_of_birth", "city"]

    def __str__(self):
        return  self.first_name + " " + self.last_name