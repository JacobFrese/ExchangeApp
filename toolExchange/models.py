from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    live = models.BooleanField(default = True)

    def serialize(self):
        return {
            "user" : {"username":self.user.username, "email":self.user.email},
            "title" : self.title,
            "description" : self.description,
            "category" : self.category,
            "price" : self.price,
            "live" : self.live,
        }
