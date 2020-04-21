from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager


class Customer(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    address_line_1 = models.CharField(max_length=250, blank=True, null=True)
    address_line_2 = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ForeignKey(
        "ImageFile", blank=True, null=True, on_delete=models.SET_NULL, related_name="+"
    )
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    # Meta Data
    created_date = models.DateTimeField(auto_now_add=True)
    last_modify_date = models.DateTimeField(auto_now=True)


class ImageFile(models.Model):
    title = models.CharField(max_length=150, blank=False, null=True)
    file = models.ImageField(upload_to="images", blank=False, null=False)
    # Meta Data
    created_date = models.DateTimeField(auto_now_add=True)
    last_modify_date = models.DateTimeField(auto_now=True)

    tags = TaggableManager()


class CustomerNote(models.Model):
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="notes"
    )
    title = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField(blank=False, null=False)
    # Meta Data
    created_date = models.DateTimeField(auto_now_add=True)
    last_modify_date = models.DateTimeField(auto_now=True)
