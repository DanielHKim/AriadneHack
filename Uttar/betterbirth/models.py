from django.db import models

class Mother(models.Model):
    phone_num = models.IntegerField(max_length=24, primary_key=True)
    mother_condition = models.CharField(max_length=128) # short description
    age = models.IntegerField(max_length=2)
    postal_code = models.CharField(max_length=8, default='0000-000') #postal code
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    give_aid = models.BooleanField(default=False) # mother-to-mother help
    receive_aid = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.first_name)

class Baby(models.Model):
    mother = models.ForeignKey(Mother)
    baby_gender = models.CharField(help_text='Gender of baby', #enum
                                    max_length=10,
                                    choices=(
                                        ('male', 'Male'),
                                        ('female', 'Female'),
                                        ('other', 'Other'),
                                    ),
                                    default='text')

    conception_datetime = models.DateTimeField(auto_now_add=True)
    birth_of_baby = models.BooleanField(default=True) # because mortality
    baby_height_cm = models.IntegerField(max_length=2) # in cm
    baby_health = models.CharField(max_length=128) # short description
    birth_datetime = models.DateTimeField(auto_now_add=True)

