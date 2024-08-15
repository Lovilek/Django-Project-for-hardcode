from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from courses.models import Group
from users.models import Subscription


@receiver(post_save, sender=Subscription)
def post_save_subscription(sender, instance: Subscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.

    """

    if created:
        course = instance.course
        groups = course.groups.annotate(student_count=Count('students'))
        if not groups.exists():

            group_to_join = Group.objects.create(course=course)
        else:
            group_to_join = groups.order_by('student_count').first()

        if group_to_join:
            group_to_join.students.add(instance.user)
        else:
            raise ValueError(f'No group to join for course {course.title}')
