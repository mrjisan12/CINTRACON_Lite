# Announcement/models.py

from django.db import models

class Announcement(models.Model):
    announcer_name = models.CharField(max_length=100, help_text="Who is making the announcement")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.announcer_name} - {self.date} {self.time.strftime('%H:%M')}"
