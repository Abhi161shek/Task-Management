from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        abstract = True  
    
class User(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
    
class Task(BaseModel):
    TASK_STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=100)  
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='Pending')
    

    assigned_users = models.ManyToManyField(User, related_name="tasks")

    def __str__(self):
        return self.name
