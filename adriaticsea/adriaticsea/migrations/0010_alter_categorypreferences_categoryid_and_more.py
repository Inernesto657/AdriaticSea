# Generated by Django 4.1.3 on 2022-11-13 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adriaticsea', '0009_alter_categorypreferences_categoryid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorypreferences',
            name='categoryId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='adriaticsea.categories', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='countrypreferences',
            name='countryId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='adriaticsea.countries', verbose_name='Countries'),
        ),
    ]
