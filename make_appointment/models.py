from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    service = models.CharField(max_length=100)

    subject = models.CharField(max_length=300)
    message = models.TextField()

    consultation = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"
