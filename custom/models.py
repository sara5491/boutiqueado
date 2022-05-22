from django.db import models


class Custom(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name