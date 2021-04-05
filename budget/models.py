from django.db import models

# Create your models here.

#create expense entry,update,delete

class Category(models.Model):
    category_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.category_name#this led to the category list in home page

class Expense(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)#category is foreignkey here which refer model "category"
    notes=models.CharField(max_length=150,null=True)
    amount=models.IntegerField()
    user=models.CharField(max_length=120)
    date=models.DateField()

    def __str__(self):
        return self.user