"""adriaticsea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adriaticsea import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.category_List),
    path('categories/<int:id>', views.category_details),
    path('users/', views.users_List),
    path('users/<int:id>', views.user_details),
    path('countries/', views.country_List),
    path('countries/keys/', views.country_keys),
    path('countries/names/', views.country_name),
    path('users/valid/<int:id>', views.isvalid_user),
    path('users/newUser/<int:id>', views.isnew_user),
    path('countriespreferences/userId/<int:id>',
         views.CountryPreference_ListbyUserId),
    path('countriespreferences/<int:id>', views.CountryPreference_details),
    path('countriespreferences/', views.CountryPreference_List),
    path('countriespreferences/Remaining/<int:id>',
         views.CountryPreference_Remaining),
    path('categoriespreferences/userId/<int:id>',
         views.CategoryPreference_ListbyUserId),
    path('categoriespreferences/<int:id>', views.CategoryPreference_details),
    path('categoriespreferences/', views.CategoryPreference_List),
    path('categoriespreferences/Remaining/<int:id>',
         views.CategoryPreference_Remaining),
    path('news/', views.New_List),
    path('news/countryId/<int:id>', views.New_ListbyCountryId),
    path('search/<str:searchTerm>/<int:id>', views.Search_News),
]

urlpatterns = format_suffix_patterns(urlpatterns)
