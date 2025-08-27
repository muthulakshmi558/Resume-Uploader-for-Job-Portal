from django.db import models
from django.core.validators import FileExtensionValidator

class Resume(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    file = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
