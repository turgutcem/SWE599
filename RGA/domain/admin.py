from django.contrib import admin
from .models import DomainKnowledge, Game,Results
from mptt.admin import MPTTModelAdmin
# Register your models here.

admin.site.register(DomainKnowledge,MPTTModelAdmin)

admin.site.register(Game)
admin.site.register(Results)
