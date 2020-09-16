from django.contrib import admin

from .models import Post, Contact

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subTitle', 'categories', 'deleted']
    search_fields = ['title', 'subTitle', 'categories', 'deleted']

    #def get_queryset(self, request):
    #    return Post.objects.filter(deleted=True)

@admin.register(Contact)
class ContactForm(admin.ModelAdmin):
    list_display = ['name', 'email',]
    