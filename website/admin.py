from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import Job, Project, PageContent, ContactSubmission, Testimonial

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'job_type', 'salary_range', 'is_published_badge', 'created_at')
    list_filter = ('is_published', 'job_type', 'department')
    search_fields = ('title', 'description', 'department')
    actions = ['publish_jobs', 'unpublish_jobs']

    def is_published_badge(self, obj):
        if obj.is_published:
            return format_html('<span style="color: #00f0ff; font-weight: bold; background: rgba(0, 240, 255, 0.1); padding: 4px 8px; border-radius: 4px;">{}</span>', 'Active')
        return format_html('<span style="color: #ff3838; font-weight: bold; background: rgba(255, 56, 56, 0.1); padding: 4px 8px; border-radius: 4px;">{}</span>', 'Draft')
    is_published_badge.short_description = 'Status'

    def publish_jobs(self, request, queryset):
        queryset.update(is_published=True)
    publish_jobs.short_description = "Publish selected job postings"

    def unpublish_jobs(self, request, queryset):
        queryset.update(is_published=False)
    unpublish_jobs.short_description = "Unpublish selected job postings"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_badge', 'is_featured', 'order', 'thumbnail_preview')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_featured')

    def category_badge(self, obj):
        colors = {
            'web': '#00f0ff',
            'software': '#b44dff',
            'uiux': '#ff00aa',
            'animation': '#ffbb00'
        }
        color = colors.get(obj.category, '#ffffff')
        return format_html('<span style="color: {color}; border: 1px solid {color}; padding: 2px 6px; border-radius: 3px; font-size: 11px; text-transform: uppercase;">{category}</span>', color=color, category=obj.get_category_display())
    category_badge.short_description = 'Category'

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{url}" style="width: 50px; height: 30px; object-fit: cover; border-radius: 3px; border: 1px solid #333;" />', url=obj.image.url)
        return "No Image"
    thumbnail_preview.short_description = 'Preview'

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'title', 'updated_at', 'updated_by')
    readonly_fields = ('updated_at', 'updated_by')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

    def section_name(self, obj):
        return obj.get_section_display()
    section_name.short_description = 'Section'

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'read_badge', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    actions = ['mark_as_read', 'mark_as_unread']

    def has_add_permission(self, request):
        return False  # Submissions come from front-end contact form only

    def read_badge(self, obj):
        if obj.is_read:
            return format_html('<span style="color: #888;">{}</span>', 'Read')
        return format_html('<span style="color: #b44dff; font-weight: bold; background: rgba(180, 77, 255, 0.15); padding: 4px 8px; border-radius: 4px; border: 1px solid #b44dff;">{}</span>', 'New Message')
    read_badge.short_description = 'Status'

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating_stars', 'is_active', 'order')
    list_filter = ('is_active', 'rating')
    search_fields = ('client_name', 'company', 'quote')
    list_editable = ('order', 'is_active')

    def rating_stars(self, obj):
        stars = '★' * obj.rating + '☆' * (5 - obj.rating)
        return format_html('<span style="color: #ffbb00; font-size: 14px;">{stars}</span>', stars=stars)
    rating_stars.short_description = 'Rating'
