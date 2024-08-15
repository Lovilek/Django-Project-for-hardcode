from jsonschema.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from courses.models import Course
from users.models import Subscription


def make_payment(request):
    """Процесс оплаты курса бонусными баллами."""
    user = request.user
    course_id = request.data.get('course_id')

    course = get_object_or_404(Course, id=course_id)

    if user.balance.balance < course.price:
        raise ValidationError('Недостаточно бонусов для покупки.')

    user.balance.balance -= course.price
    user.balance.save()

    subscription = Subscription.objects.create(user=user, course=course)

    return subscription


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or Subscription.objects.filter(user=request.user).exists()

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or Subscription.objects.filter(user=request.user, course=obj.course).exists()


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS
