from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_ratelimit.decorators import ratelimit
from .models import Project, Testimonial, Job, PageContent
from .forms import ContactForm

def homepage(request):
    # Fetch data
    projects = Project.objects.filter(is_featured=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    jobs = Job.objects.filter(is_published=True)
    
    # Get editable page content sections or use defaults if they don't exist yet
    about_content = PageContent.objects.filter(section='about').first()
    services_content = PageContent.objects.filter(section='services').first()
    stats_content = PageContent.objects.filter(section='stats').first()

    # Form initialization
    form = ContactForm()
    
    context = {
        'projects': projects,
        'testimonials': testimonials,
        'jobs': jobs,
        'about_content': about_content,
        'services_content': services_content,
        'stats_content': stats_content,
        'form': form
    }
    return render(request, 'index.html', context)

@ratelimit(key='ip', rate='3/m', method='POST', block=True)
@require_POST
def contact_submit(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Your message has been securely transmitted. Our development team will review it and contact you shortly.'
        })
    else:
        errors = {field: error_list[0] for field, error_list in form.errors.items()}
        return JsonResponse({
            'success': False,
            'errors': errors
        }, status=400)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('website:homepage')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('website:homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('website:homepage')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('website:homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_logout(request):
    auth_logout(request)
    return redirect('website:homepage')
