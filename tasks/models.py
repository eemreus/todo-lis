# tasks/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    priority = models.CharField(
        max_length=10,
        choices=[
            ("Yüksek", "Yüksek"),
            ("Orta", "Orta"),
            ("Düşük", "Düşük")
        ],
        default="Orta"
    )
    completed = models.BooleanField(default=False)  # ✅ Bu satırı ekledik

    def __str__(self):
        return self.title
