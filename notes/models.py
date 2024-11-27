from django.db import models

from django.contrib.auth.models import User

class Task(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    due_date=models.DateTimeField(null=True)

    category_choices=(
        ("personal","personal"),
        ("business","business")
    )

    category=models.CharField(max_length=200,choices=category_choices,default="personal")

    status_choices=(
        ("pending","pending"),
        ("in-progress","in-progress"),
        ("done","done")
    )

    status=models.CharField(max_length=200,choices=status_choices,default="pending")

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    

    def __str__(self) -> str:
        
        return self.title


