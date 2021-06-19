from django.contrib import admin
from .models import DomainKnowledge, Game
from mptt.admin import MPTTModelAdmin
# Register your models here.

admin.site.register(DomainKnowledge,MPTTModelAdmin)

admin.site.register(Game)
