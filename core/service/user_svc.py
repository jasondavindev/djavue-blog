from django.contrib.auth.models import User
from django.contrib import auth
from core.service import log_svc


def login(request, username, password):
    user = auth.authenticate(username=username, password=password)
    user_dict = None

    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = toJSON(user)

    return user_dict

def logout(request):
  if request.user.is_authenticated():
      log_svc.log_logout(request.user)
      auth.logout(request)
      return {}

  return None


def create_account(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']

    try:
      user = auth.models.User.objects.create_user(
          username, email=email, password=password, first_name=first_name, last_name=last_name)
        
      userDict = toJSON(user)
      userDict['created'] = True
      return userDict
    except:
      return { 'created': False }


def whoami(user):
    i_am = {
        'user': toJSON(user),
        'authenticated': True,
    } if user.is_authenticated() else {'authenticated': False}
    
    return i_am


def toJSON(user):
    return {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }
