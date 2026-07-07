from django.db import migrations
import json

def seed_data(apps, schema_editor):
    Project = apps.get_model('website', 'Project')
    Job = apps.get_model('website', 'Job')
    Testimonial = apps.get_model('website', 'Testimonial')
    PageContent = apps.get_model('website', 'PageContent')
    
    # 1. Seed Projects
    Project.objects.create(
        title="Finding & Classifying Cyber Threads",
        category="software",
        description="A Machine Learning model to find and classify cyber-threads using a predefined dataset. Achieved successful model output and identification.",
        image="projects/project_software.png",
        is_featured=True,
        order=1
    )
    Project.objects.create(
        title="ESCTRIX SMS",
        category="software",
        description="An end-to-end encrypted, IP-based calling and chatting web application enabling secure, peer-to-peer global data transfer without email or phone verification.",
        image="projects/project_software.png",
        is_featured=True,
        order=2
    )
    Project.objects.create(
        title="AI Resume Shortlisting",
        category="software",
        description="An AI-powered recruitment platform designed to process resumes using NLP keyword extraction, candidates profile images with Pillow, and run a custom API for ATS scoring.",
        image="projects/project_software.png",
        is_featured=True,
        order=3
    )
    Project.objects.create(
        title="Real-Time Error Handling Bot",
        category="software",
        description="An AI-powered programming assistant desktop app that helps developers write, test, and troubleshoot Python code seamlessly using Google Gemini AI.",
        image="projects/project_software.png",
        is_featured=True,
        order=4
    )
    Project.objects.create(
        title="Personal Portfolio Website",
        category="web",
        description="Developed a comprehensive personal portfolio website to showcase professional skills, education, and projects with a responsive, modern aesthetic.",
        image="projects/project_mobile_app.png",
        is_featured=True,
        order=5
    )
    Project.objects.create(
        title="Tourist Guide Platform",
        category="web",
        description="Designed and developed a Tourist Guide website for college web development competition featuring interactive navigation and detailed guides.",
        image="projects/project_uiux.png",
        is_featured=True,
        order=6
    )

    # 2. Seed Jobs
    Job.objects.create(
        title="Python/Django Backend Developer",
        department="Engineering",
        location="Remote",
        job_type="full-time",
        description="We are seeking an experienced Django developer to construct robust backend APIs and handle database migrations. Proficiencies in RESTful patterns and security architecture are critical.",
        salary_range="₹6,00,000 - ₹9,00,000 / year",
        contact_email="esctrix369@gmail.com",
        is_published=True
    )
    Job.objects.create(
        title="UI/UX Designer",
        department="Design",
        location="Remote",
        job_type="contract",
        description="Looking for a visual designer skilled in Figma and Adobe Photoshop who loves dark mode and futuristic aesthetic systems. Must be able to deliver premium wireframes and responsive assets.",
        salary_range="₹40,000 - ₹60,000 / month",
        contact_email="esctrix369@gmail.com",
        is_published=True
    )

    # 3. Seed Testimonials
    Testimonial.objects.create(
        client_name="Alex Chen",
        company="CEO, Nexus Health",
        quote="EscTrix delivered an exceptional API platform in record time. Their code structure is robust, and the frontend animations completely elevated our startup brand. Highly recommended.",
        rating=5,
        is_active=True,
        order=1
    )
    Testimonial.objects.create(
        client_name="Sophia Martinez",
        company="Product Lead, Aether Graphics",
        quote="The UI/UX design provided by EscTrix was breathtaking. They captured our dark futuristic brand perfectly. Their team communicates clearly and delivers precise execution on every sprint.",
        rating=5,
        is_active=True,
        order=2
    )

    # 4. Seed PageContent
    PageContent.objects.create(
        section="about",
        title="Architecting Tomorrow's Solutions Today",
        content={
            "paragraphs": [
                "We are a forward-thinking digital product agency founded by Jeyakanthan. We don't just write code; we design futuristic experiences, build highly optimized web platforms, and design premium user experiences tailored to high-growth startups and visionary companies.",
                "Our core philosophy centers around speed, security, and next-level aesthetic execution. We specialize in bringing complex ideas to life through robust backend systems and stunning animations."
            ]
        }
    )

def remove_data(apps, schema_editor):
    Project = apps.get_model('website', 'Project')
    Job = apps.get_model('website', 'Job')
    Testimonial = apps.get_model('website', 'Testimonial')
    PageContent = apps.get_model('website', 'PageContent')
    
    Project.objects.all().delete()
    Job.objects.all().delete()
    Testimonial.objects.all().delete()
    PageContent.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
