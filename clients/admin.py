from django.contrib import admin
from .models import Client
from .models import Client, Comment

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    model = Client
class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
