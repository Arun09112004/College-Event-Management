from django.db import models

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]

class Registration(models.Model):
    student_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.student_name