from celery import shared_task
from .models import UserProfile

@shared_task
def update_profile_task(profile_id, profile_image, full_name, email):
    profile = UserProfile.objects.get(pk=profile_id)

    if profile_image:
        profile.profile_image = profile_image

    if full_name:
        profile.full_name = full_name

    if email:
        profile.email = email

    profile.save()