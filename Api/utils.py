from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
 return  user.is_staff

def admin_only(view_func):
    return user_passes_test(is_admin)(view_func)
