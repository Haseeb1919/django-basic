from django.db import models

# Create your models here.
#model to create todo list 
class TodoList(models.Model):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

#model to create todo item
class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text
