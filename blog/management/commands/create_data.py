from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from faker import Faker
from random import randint, choice
from blog.models import Post, Comment

User = get_user_model()

password = 'zxcvbnm8'
text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae ipsum vitae ipsum condimentum maximus. Curabitur volutpat purus vel ante porta, sit amet sagittis nisl pharetra. Sed a fermentum diam, non efficitur neque. Nullam nec iaculis leo, quis ornare purus. In tincidunt tempor fermentum. Vivamus tristique lobortis commodo. Mauris eleifend dolor sed rutrum convallis. Sed rutrum vehicula lobortis. Maecenas a tortor imperdiet, consectetur augue vel, pharetra justo. Morbi pharetra mattis risus, non luctus metus posuere id. Duis molestie ligula sed tempus sagittis.

Aenean faucibus diam eu venenatis pharetra. In hac habitasse platea dictumst. Phasellus efficitur nisl nec nulla convallis, sit amet aliquet enim tempor. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce malesuada, augue non placerat molestie, nisi tellus facilisis diam, eu viverra mauris elit non massa. Donec augue lorem, volutpat in malesuada in, sagittis nec libero. Phasellus gravida velit eu varius dignissim. Nulla pretium sapien efficitur, euismod tortor a, dignissim eros.

Maecenas facilisis purus vitae dolor eleifend, ut ultrices velit pulvinar. Nullam elementum tortor nec urna scelerisque, vel scelerisque nisi faucibus. Pellentesque eleifend metus leo, id dapibus ipsum ullamcorper quis. Quisque iaculis nisl metus, ut lobortis sapien hendrerit non. Maecenas iaculis finibus nibh fringilla sodales. Nunc quis aliquet odio. Maecenas ut congue nisl. Aenean dignissim magna sem. Vivamus nec magna pulvinar, sodales sapien vel, facilisis turpis. Donec porta quis lectus vel placerat. Integer vel gravida ante. Nulla id scelerisque ipsum, id auctor ipsum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nulla facilisi.'''
com = ['Good post!', 'Not bad', 'Cool!!', 'I did not like', 'poorly']

class Command(BaseCommand):
    help = 'This command create data, has one argument "count_data"'

    def add_arguments(self, parser):
        parser.add_argument('count_data', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        num = options['count_data']


        for _ in range(10):
            user = User.objects.create_user(username=fake.name(), email=fake.email(), password=password)
            user.is_superuser = False
            user.is_staff = False
            user.save()
        authors_id = User.objects.values_list('id', flat=True)

        list_obj_post = []
        for i in range(1, num+1):
            post = Post(
                author_id=choice(authors_id),
                title=f'Post{i}',
                content=text,
            )
            list_obj_post.append(post)
        Post.objects.bulk_create(list_obj_post)
        post_id = Post.objects.values_list('id', flat=True)

        commets_obj_list = []
        for _ in range(num):
            comments = Comment(
                author_id=authors_id,
                comment=choice(com),
                post_id=choice(post_id),
                is_published=True
            )
            commets_obj_list.append(comments)
        Comment.objects.bulk_create(commets_obj_list)

        self.stdout.write(self.style.SUCCESS(f'Success create data count {num}'))