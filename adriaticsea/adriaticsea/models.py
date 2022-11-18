from django.db import models

class Categories (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Users (models.Model):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    emailId =  models.CharField(max_length=500)
    profilePicture = models.CharField(max_length=1000)
    countries=models.TextField(null=True)
    categories=models.TextField(null=True)
    def __str__(self):
        return self.firstname+' '+self.lastname

class Countries(models.Model):
    countryName= models.CharField(max_length=100,null=True,blank=True)
    countryKey = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
            return self.countryName


class CountryPreferences(models.Model):
    user = models.ForeignKey(Users, default=1, verbose_name="Users", on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, default=1, verbose_name="Countries", on_delete=models.CASCADE)
    
    def __str__(self):
            return str(self.user.firstname) +' '+ str(self.user.lastname) + ' - ' + str(self.country.countryName)


class CategoryPreferences(models.Model):
    user = models.ForeignKey(Users, default=1, verbose_name="Users", on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, default=1, verbose_name="Categories", on_delete=models.CASCADE)
    
    def __str__(self):
            return str(self.user.firstname) +' '+ str(self.user.lastname) + ' - ' + str(self.category.name)


class News(models.Model):
    country = models.ForeignKey(Countries, default=1, verbose_name="Countries", on_delete=models.CASCADE)
    trend =  models.CharField(max_length=80,null=True)
    title =  models.CharField(max_length=100)
    image =  models.CharField(max_length=200)
    posted = models.CharField(max_length=50)
    posteddatetime =  models.DateTimeField(null=True)
    detailednews =  models.TextField(max_length=500)
    description =  models.TextField(max_length=500)
    
    def __str__(self):
            return self.country.countryName +' - '+ self.title