from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

CHARS_LIMIT: int = 30
MAX_LENGTH: int = 256


class Group(models.Model):
    """Model for groups."""
    title = models.CharField(
        'Название',
        max_length=MAX_LENGTH
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True
    )
    description = models.TextField(
        'Описание'
    )

    class Meta:
        """Inner Meta class of Group model."""
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'
        ordering = ('id',)

    def __str__(self):
        """Displays Group title in admin panel."""
        return self.title[:CHARS_LIMIT]


class Post(models.Model):
    """Model for posts."""
    text = models.TextField(
        'Текст'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True
    )

    class Meta:
        """Inner Meta class of Post model."""
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)

    def __str__(self):
        """Displays Post text in admin panel."""
        return self.text[:CHARS_LIMIT]


class Comment(models.Model):
    """Model for post's comments."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        'Текст'
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        """Inner Meta class of Comment model."""
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('id',)

    def __str__(self):
        """Displays Comment text in admin panel."""
        return self.text[:CHARS_LIMIT]
