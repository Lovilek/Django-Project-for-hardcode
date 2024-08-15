from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователи'
    )
    balance = models.PositiveIntegerField(
        default=1000,
        verbose_name='Баланс'
    )

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)

    def __str__(self):
        return f'Баланс {self.user.get_full_name()} - {self.balance}'

    def save(self, *args, **kwargs):
        if self.balance < 0:
            self.balance = 0
        super().save(*args, **kwargs)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователи'
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Начало подписки'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)

    def __str__(self):
        return f'Подписка {self.user.get_full_name()} на курс {self.course.title}'
