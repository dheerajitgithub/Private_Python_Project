from django.db import models

class User_details(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class User_Address(models.Model):
    user = models.ForeignKey(User_details,on_delete=models.CASCADE,related_name='addresses')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


    def __str__(self) -> str:
        return f"{self.city},{self.state},{self.country}"

