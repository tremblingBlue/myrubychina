from django.contrib import admin
from .models import Node, Article

class NodeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Base', {'fields': ['node_name']}),
        ('Parent', {'fields': ['parent']}),
        ('Date', {'fields': ['create_date', 'modify_date']})
    ]

admin.site.register(Node, NodeAdmin)
admin.site.register(Article)