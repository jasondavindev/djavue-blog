from core.models import User


def create_user():
    return User.objects.create_user(
        username='test',
        password='test',
        email='test@mail.com',
        first_name='test',
        last_name='bot',
    )

def get_post():
    return {
        'title': 'my post',
        'body': 'my body'
    }

def get_comment():
    return {
        'comment': 'hello world!',
        'post': 1,
    }