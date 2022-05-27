from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

from products.models import Product


class ProductReview(models.Model):
    """ Add ProductReview table to database """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        null=False, related_name='product')
    review_content = models.TextField(
        null=False, blank=False, validators=[MaxLengthValidator(250)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date_added = models.DateField(
        auto_now_add=True, null=False, blank=False, editable=False
    )