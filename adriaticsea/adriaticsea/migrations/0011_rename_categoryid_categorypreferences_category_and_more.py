# Generated by Django 4.1.3 on 2022-11-13 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adriaticsea', '0010_alter_categorypreferences_categoryid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorypreferences',
            old_name='categoryId',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='categorypreferences',
            old_name='userId',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='countrypreferences',
            old_name='countryId',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='countrypreferences',
            old_name='userId',
            new_name='user',
        ),
    ]
