from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

# Получаем модель пользователя
User = get_user_model()

class Review(models.Model):
    """
    Модель для хранения отзывов, которые клиенты оставляют риелторам.
    """
    # Внешний ключ на риелтора
    realtor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_received',
        verbose_name='Риелтор'
    )

    # Внешний ключ на клиента
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_given',
        verbose_name='Клиент'
    )

    # Текст отзыва
    text = models.TextField(verbose_name='Текст отзыва')

    # Оценка от 1 до 5
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Оценка'
    )

    # Дата создания отзыва
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        # Один отзыв от клиента на одного риелтора
        unique_together = ('realtor', 'client')

    def __str__(self):
        return f"Отзыв от {self.client} на {self.realtor} (Оценка: {self.rating})"