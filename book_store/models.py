from datetime import datetime
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    info = models.CharField(max_length=5000)
    ISBN = models.CharField(max_length=20) #primary key?
    publish_date = models.DateField(default=datetime.now)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    app_label = "book_store"
    model_name = "book"

    def __str__(self):
        return self.title


class RequestRecord(models.Model):
    path = models.URLField()
    time = models.DateTimeField(default=datetime.now)

    @classmethod
    def get_last_10_items(cls):
        return cls.objects.order_by('-id')[:10]

    def __str__(self):
        return self.time.strftime('[%d/%b/%Y %H:%M:%S] - ') + self.path

