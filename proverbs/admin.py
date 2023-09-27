from django.contrib import admin
from proverbs.models import Proverb,Origin,OriginConnection


# Register your models here.

admin.site.register([Proverb,Origin,OriginConnection])
