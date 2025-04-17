from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
     # Replace 'username' with 'email' as the unique identifier
    username = None  # Remove the username field
    email = models.EmailField(unique=True)  # Make email unique

    # Specify that email should be the unique identifier
    USERNAME_FIELD = 'email'  # This tells Django to use email as the identifier
    REQUIRED_FIELDS = ['full_name']  # Email and full_name are required fields for creating a superuser

    full_name = models.CharField(max_length=255)



class UserProfile(models.Model):


    DEPARTMENTS = (
        ('CSE','CSE'),
        ('EEE','EEE'),
        ('CIVIL','CIVIL'),
        ('PHARM','PHARM'),
        ('LLB','LLB'),
        ('ENGLISH','ENGLISH'),
        ('ARC','ARC'),
        ('BBA','BBA'),
    )

    SEMESTERS = (
        ('1.1','1.1'),
        ('1.2','1.2'),
        ('2.1','2.1'),
        ('2.2','2.2'),
        ('3.1','3.1'),
        ('3.2','3.2'),
        ('4.1','4.1'),
        ('4.2','4.2'),
        ('M.Sc','M.Sc'),
        ('MBA','MBA'),
        ('GRADUATE','GRADUATE'),
    )

    SECTIONS = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('E','E'),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, choices=DEPARTMENTS)
    semester = models.CharField(max_length=10, choices=SEMESTERS)
    section = models.CharField(max_length=10, choices=SECTIONS)
    batch_no = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=15)
    blood_grp = models.CharField(max_length=15)
    points = models.IntegerField(default=0)
    facebook_link = models.CharField(max_length=255)
    instragram_link = models.CharField(max_length=255)
    linkedin_link = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.full_name} - Profile'
