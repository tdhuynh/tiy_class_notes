from django.contrib import admin
from menu_api.models import Special, Ingredient

admin.site.register([Special, Ingredient])
