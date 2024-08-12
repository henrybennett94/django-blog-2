from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"

"""
Models for shopping app-
    from my-shopping-
class List(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="shopping_list"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{list.title}"

    from my-shopping-app-
class Items(models.Model):
    label = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    shop_list = models.CharField(max_length=100, blank=True, null=True)
    shop_item = models.CharField(max_length=100)
    created_on = models.DateTimeField('created on', auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shop_list} {self.created_on}"
"""

