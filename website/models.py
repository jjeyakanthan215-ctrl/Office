from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    JOB_TYPES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
    ]
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100, help_text="e.g. Engineering, Design, Animation")
    location = models.CharField(max_length=100, default="Remote")
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='remote')
    description = models.TextField(help_text="Detailed job description and requirements")
    salary_range = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. $80,000 - $100,000")
    contact_email = models.EmailField(default="careers@esctrix.com", help_text="Where application emails should go")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_job_type_display()})"

    class Meta:
        ordering = ['-created_at']

class PageContent(models.Model):
    SECTION_CHOICES = [
        ('about', 'About Us Section'),
        ('services', 'Services Section'),
        ('stats', 'Stats Section'),
    ]
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    content = models.JSONField(help_text="Flexible JSON content structure for this section")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.get_section_display()

    class Meta:
        verbose_name = "Page Content"
        verbose_name_plural = "Page Contents"

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('software', 'Software Development'),
        ('uiux', 'UI/UX Design'),
        ('animation', 'Animation & Motion'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Upload project thumbnail image")
    link = models.URLField(blank=True, null=True, help_text="Link to live project or case study")
    is_featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', '-created_at']

class ContactSubmission(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

    class Meta:
        ordering = ['-created_at']

class Testimonial(models.Model):
    client_name = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    quote = models.TextField()
    rating = models.IntegerField(default=5, help_text="Rating from 1 to 5 stars")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.client_name} - {self.company}"

    class Meta:
        ordering = ['order']
