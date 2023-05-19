from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='book_covers/')
    count_get = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view', args=(self.id, ), )


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text




