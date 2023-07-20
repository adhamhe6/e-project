from django.contrib.auth.models import User

def get_user_info(request):
    user_info = None
    if request.user.is_authenticated:
        user_info = User.objects.get(pk=request.user.pk)
    return {'user_info': user_info}