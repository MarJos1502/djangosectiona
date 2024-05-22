from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True, blank=False)  # BIGINT NOT NULL AUTO INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55, blank=False)  # VARCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

    class Meta:
       db_table = 'genders'

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False)  # BIGINT NOT NULL AUTO INCREMENT PRIMARY KEY
    first_name = models.CharField(max_length=55, blank=False)  # VARCHAR(55) NOT NULL
    middle_name = models.CharField(max_length=55, blank=True)  # VARCHAR(55) NULL
    last_name = models.CharField(max_length=55, blank=False)  # VARCHAR(55) NOT NULL
    age = models.IntegerField(blank=False)  # INTEGER
    birth_date = models.DateField(blank=False)  # DATE
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)  # Foreign key to Gender
    username = models.CharField(max_length=55, blank=False )  # VARCHAR(55) NOT NULL
    password = models.CharField(max_length=255, blank=False)  # VARCHAR(255) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True)  # TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True)  # TIMESTAMP DEFAULT CURRENT TIMESTAMP ON UPDATE CURRENT TIMESTAMP

    class Meta:
        db_table = 'users'  # Table name in the database



