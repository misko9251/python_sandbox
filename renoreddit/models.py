from django.db import models
from django.utils import timezone # takes our timezone settings into consideration
from django.contrib.auth.models import User # user is a separate table so we must import the user model


# To make changes to DB, you must run migrations (python3 manage.py makemigrations)
# To view the SQL code you can run the migration number (python3 manage.py sqlmigrate renoreddit 0001)
# Then, run the migration to make the changes (python3 manage.py migrate)
# Migrations are useful bc we can make changes to our DB even after it is created and has data, if we didnt have a way to do this, we would have to run complicated SQL code to update our DB structure. Migrations allow us to make whatever changes we need


# "Post" model below - a class that inherits from django model class

class Post(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField(default='') # similar to CharField, but textfield is unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete with this value is a one way street, if a user is deleted entirely, all of their posts will also be deleted

    # Below allows us to return just the title of the post in python shell
    def __str__(self):
        return self.title


