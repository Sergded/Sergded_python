from django.dispatch import receiver
from django.db.models.signals import post_save
from posts.models import Posts


@receiver(post_save,sender = Posts)
def post_save_user(sender,instance,**kwargs):
    if Posts.objects.filter(category = instance.category).count() <= CATEGORY.get(instance.category,DEFAULT):
        print("User created")
    else:
        if Posts.objects.filter(category = instance.category).order_by('time_create').first().delete():
            print("User deleted")


CATEGORY = {
    'actors' : 6,
    'singers' : 3
}

DEFAULT=1
