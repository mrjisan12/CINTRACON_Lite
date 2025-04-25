from django.db import models
from authentication.models import CustomUser

class Semester(models.Model):
    name = models.CharField(max_length=10)  # Example: '1.1', '1.2', '2.1' etc.

    def __str__(self):
        return self.name

class Note(models.Model):
    semester = models.ForeignKey(Semester, related_name='notes', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # This is fine (note name)
    description = models.CharField(max_length=150)
    page_no = models.IntegerField()
    file = models.FileField(upload_to='notes/')  # Files will be saved under /media/notes/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.semester.name})"  # 'name' not 'title'
