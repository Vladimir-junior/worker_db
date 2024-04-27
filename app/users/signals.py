from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, Position

@receiver(post_save, sender=User)
def update_position_employees_count_on_create(sender, instance, created, **kwargs):
    if created:
        position = instance.position
        if position:
            position.employees_count = position.user_set.count()
            position.save()

@receiver(post_delete, sender=User)
def update_position_employees_count_on_delete(sender, instance, **kwargs):
    position = instance.position
    if position:
        position.employees_count = position.user_set.count()
        position.save()
