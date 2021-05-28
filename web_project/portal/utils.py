from django.contrib.auth.models import User


def get_or_create_ghost_user() -> User:
    user, _ = User.objects.get_or_create(
        username="ghost", first_name="Anonymous", last_name="Anonymous"
    )
    return user
