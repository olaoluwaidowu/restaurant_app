from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings


def send_confirmation_email(request, user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    message = f'Click the link below to complete your registration:\n'
    message += f'http://http://127.0.0.1:8000/auth/activate/{uid}/{token}/'
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])
    return


# message += f'http://{current_site.domain}/activate/{uid}/{token}/'