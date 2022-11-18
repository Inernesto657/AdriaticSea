from os import stat
from re import search
from django.http import JsonResponse
from .models import Categories, Countries, Users, CountryPreferences, CategoryPreferences, News
from .serializers import CategorySerializer, CountrySerializer, UserSerializer, CountryPreferenceSerializer, CategoryPreferenceSerializer, NewSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import permissions


@api_view(['GET', 'POST'])
def category_List(request, format=None):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_details(request, id, format=None):
    try:
        category = Categories.objects.get(pk=id)
    except Categories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
def users_List(request, format=None):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                oUser = Users.objects.filter(
                    emailId__iexact=request.data['emailId']).all()
                if (oUser.count() > 0):
                    serializer = UserSerializer(oUser.first())
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
                else:
                    SerializerResponse = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Users.DoesNotExist:
                print(serializer.errors)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, id, format=None):
    try:
        user = Users.objects.get(pk=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            try:
                count = Users.objects.filter(
                    emailId__iexact=request.data['emailId']).count()
                if (count > 0):
                    print("request.data.get('countries')",
                          request.data.get('countries') == None)
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer.save()
                    userObj = Users.objects.filter(
                        emailId__iexact=request.data['emailId'])
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Users.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def country_keys(request, format=None):
    if (request.method == 'GET'):
        keys = Countries.objects.values('id', 'countryKey')
        print(keys)
        # serializer = CountrySerializer(keys,many=True)
        # return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(keys, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def country_name(request, format=None):
    if (request.method == 'GET'):
        print('In get method')
        keys = Countries.objects.values('id', "countryName")
        return Response(keys, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def country_List(request, format=None):
    if (request.method == 'GET'):
        countries = Countries.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def isvalid_user(request, id, format=None):
    if (request.method == 'GET'):
        try:
            user = Users.objects.get(pk=id)
            return Response(True, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response(False, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def isnew_user(request, id, format=None):
    if (request.method == 'GET'):
        try:
            user = Users.objects.get(pk=id)
            print(user)
            return Response(True, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response(False, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'DELETE'])
def CountryPreference_details(request, id, format=None):
    try:
        countryPreference = CountryPreferences.objects.get(pk=id)
    except CountryPreferences.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        serializer = CountryPreferenceSerializer(countryPreference)
        return Response(serializer.data)
    elif (request.method == 'DELETE'):
        countryPreference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
def CountryPreference_List(request, format=None):
    if request.method == 'GET':
        countryPreferences = CountryPreferences.objects.all()
        serializer = CountryPreferenceSerializer(countryPreferences, many=True)
        return Response(serializer.data)
    if request.method == 'PUT':
        oUser = Users.objects.filter(id=request.data['user'])
        oCountry = Countries.objects.filter(id=request.data['country'])
        serializer = CountryPreferenceSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as exception:
                print(exception)
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def CountryPreference_ListbyUserId(request, id, format=None):
    if request.method == 'GET':
        countryPreferences = CountryPreferences.objects.all()
        countryPreferences = [
            x for x in countryPreferences.all() if x.user.id == id]
        serializer = CountryPreferenceSerializer(countryPreferences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def CountryPreference_Remaining(request, id, format=None):
    if request.method == 'GET':
        allCountries = Countries.objects.all()
        countryPreferences = CountryPreferences.objects.all()
        countryPreferences = [
            x for x in countryPreferences.all() if x.user.id == id]
        filteredCountryPreferences = []
        for ctry in allCountries:
            ctryList = [
                y for y in countryPreferences if y.country.id == ctry.id]
            if not ctryList:
                filteredCountryPreferences.append(ctry)

        serializer = CountrySerializer(filteredCountryPreferences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def CategoryPreference_details(request, id, format=None):
    try:
        categoryPreference = CategoryPreferences.objects.get(pk=id)
    except CategoryPreferences.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        serializer = CategoryPreferenceSerializer(categoryPreference)
        return Response(serializer.data)
    elif (request.method == 'DELETE'):
        categoryPreference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
def CategoryPreference_List(request, format=None):
    if request.method == 'GET':
        categoryPreferences = CategoryPreferences.objects.all()
        serializer = CategoryPreferenceSerializer(
            categoryPreferences, many=True)
        return Response(serializer.data)
    if request.method == 'PUT':
        oUser = Users.objects.filter(id=request.data['user'])
        oCategory = Categories.objects.filter(id=request.data['category'])
        serializer = CategoryPreferenceSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as exception:
                print(exception)
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def CategoryPreference_ListbyUserId(request, id, format=None):
    if request.method == 'GET':
        categoryPreferences = CategoryPreferences.objects.all()
        categoryPreferences = [
            x for x in categoryPreferences.all() if x.user.id == id]
        serializer = CategoryPreferenceSerializer(
            categoryPreferences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def CategoryPreference_Remaining(request, id, format=None):
    if request.method == 'GET':
        allCategories = Categories.objects.all()
        categoryPreferences = CategoryPreferences.objects.all()
        categoryPreferences = [
            x for x in categoryPreferences.all() if x.user.id == id]
        filteredCategoryPreferences = []
        for ctgry in allCategories:
            ctgryList = [
                y for y in categoryPreferences if y.category.id == ctgry.id]
            if not ctgryList:
                filteredCategoryPreferences.append(ctgry)

        serializer = CategorySerializer(filteredCategoryPreferences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def New_List(request, format=None):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = NewSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as exception:
                print(exception)
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        News.objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def New_ListbyCountryId(request, id, format=None):
    if request.method == 'GET':
        news = News.objects.all()
        news = [x for x in news.all() if x.country.id == id]
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Search_News(request, searchTerm, id, format=None):
    if request.method == 'GET':
        news = News.objects.all()
        news = [x for x in news.all() if searchTerm in x.trend and x.country.id == id]
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
