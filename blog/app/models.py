from django.db import models

class Post(models.Model):
    TECH = (
        ('Tecnologia', 'TC'),
        ('Curiosidades', 'CR'),
        ('Geral', 'GR'),
    )
    title = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.CharField(max_length=12, choices=TECH)
    deleted = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


