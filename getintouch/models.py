from django.db import models

class ContactMessage(models.Model):
    PROJECT_TYPES = (
        ('web_design', 'Web Design'),
        ('mobile_app', 'Mobile App'),
        ('graphic_design', 'Graphic Design'),
        ('other', 'Other'),
    )
       
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    city = models.CharField(max_length=100, null=True)
    project_type = models.CharField(max_length=100, choices=PROJECT_TYPES, null=True)
    description = models.TextField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = 'getintouch'
