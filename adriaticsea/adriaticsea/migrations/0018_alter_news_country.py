# Generated by Django 4.1.3 on 2022-11-14 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adriaticsea', '0017_alter_categorypreferences_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adriaticsea.countries', verbose_name='Countries'),
        ),
    ]
