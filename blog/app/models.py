from django.db import models

class Category(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices = Category.choices,
        default = Category.GR
    )
    deleted = models.BooleanField(default=True)

    def get_category_label(self):
        return self.get_categories_display()

    def __str__(self):
        return self.title


