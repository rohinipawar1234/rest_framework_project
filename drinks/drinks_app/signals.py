# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import CustomUser

@receiver(post_save, sender = CustomUser)
def send_login_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Excited to Have You at Drink Application!'
        html_message = render_to_string('registration_email.html', {'user': instance})
        plain_message = strip_tags(html_message)
        from_email = 'rohinipawar49363@gmail.com'
        to_email = [instance.email]
        send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
