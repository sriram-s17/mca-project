from django.contrib.auth.models import User
def get_users(request):
    users = User.objects.all()
    return {
        'users': users
    }