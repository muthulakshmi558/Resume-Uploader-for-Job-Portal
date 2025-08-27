from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'file']

    def clean_file(self):
        f = self.cleaned_data.get('file')
        if not f:
            raise forms.ValidationError("No file uploaded.")
        # MIME check (extra safety)
        valid_mime = [
            'application/pdf',
            'application/msword',  # .doc
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',  # .docx
        ]
        if hasattr(f, 'content_type') and f.content_type not in valid_mime:
            raise forms.ValidationError("Unsupported file type.")
        # Size limit: 5 MB (adjust if you want)
        max_size = 5 * 1024 * 1024
        if f.size > max_size:
            raise forms.ValidationError("File too large (max 5MB).")
        return f
