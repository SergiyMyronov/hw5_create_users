from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Creating some random users'

    def add_arguments(self, parser):
        parser.add_argument('num', type=int, help='Number of new users')

    def handle(self, *args, **kwargs):
        num = kwargs['num']
        if num < 1 or num > 10:
            self.stdout.write(self.style.ERROR('Error - number of users must be in the range [1..10]'))
            return

        obj_list = []
        user_model = get_user_model()
        for i in range(num):
            usr_name = get_random_string()
            pwd = make_password(usr_name)
            obj_list.append(
                user_model(
                    username=usr_name,
                    email=usr_name+'@'+'gmail.com',
                    password=pwd)
            )
        user_model.objects.bulk_create(obj_list)
        self.stdout.write(self.style.SUCCESS('%s user(s) created' % num))
