from django.conf import settings
from django.core.mail import send_mail


def send_email(subject: str, message: str, recipient_list: list[str]) -> None:
    if (
        settings.EMAIL_HOST_USER
        and settings.EMAIL_HOST_PASSWORD
        and len(recipient_list) > 0
    ):
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
