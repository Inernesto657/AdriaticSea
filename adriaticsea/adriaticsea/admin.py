from django.contrib import admin
from .models import Categories
from .models import Users
from .models import Countries
from .models import CountryPreferences
from .models import CategoryPreferences
from .models import News

admin.site.register(Categories)
admin.site.register(Users)
admin.site.register(Countries)
admin.site.register(CountryPreferences)
admin.site.register(CategoryPreferences)
admin.site.register(News)