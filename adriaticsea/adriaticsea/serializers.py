from dataclasses import field
from rest_framework import serializers
from .models import Categories, Users, Countries, CountryPreferences, CategoryPreferences, News

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','name','description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','firstname','lastname','emailId','profilePicture','countries','categories']
        # read_only_fields=('is_new')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['id','countryName','countryKey']

class CountryPreferenceSerializer(serializers.ModelSerializer):
    user =  serializers.PrimaryKeyRelatedField(queryset= Users.objects.all(),many=False)
    country = serializers.PrimaryKeyRelatedField(queryset= Countries.objects.all(),many=False)
    # user=UserSerializer(
    #     read_only=True,
    #     many=True
    # )

    # country=CountrySerializer(
    #     read_only=True,
    #     many=True
    # )

    class Meta:
        fields = ['id','user','country']
        model = CountryPreferences

class CategoryPreferenceSerializer(serializers.ModelSerializer):
    # user=UserSerializer(
    #     read_only=True,
    #     many=True
    # )
    user =  serializers.PrimaryKeyRelatedField(queryset= Users.objects.all(),many=False)

    # category=CategorySerializer(
    #     read_only=True,
    #     many=True
    # )
    category = serializers.PrimaryKeyRelatedField(queryset= Categories.objects.all(),many=False)
    class Meta:
        model = CategoryPreferences
        fields = ['id','user','category']

class NewSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset= Countries.objects.all(),many=False)
    
    class Meta:
        model = News
        fields = ['country','trend','title','image','posted','posteddatetime','detailednews','description']