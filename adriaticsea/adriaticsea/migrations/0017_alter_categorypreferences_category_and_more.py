# Generated by Django 4.1.3 on 2022-11-14 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adriaticsea', '0016_rename_time_news_posteddatetime_news_trend_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorypreferences',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adriaticsea.categories', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='categorypreferences',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adriaticsea.users', verbose_name='Users'),
        ),
        migrations.AlterField(
            model_name='countrypreferences',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adriaticsea.countries', verbose_name='Countries'),
        ),
        migrations.AlterField(
            model_name='countrypreferences',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adriaticsea.users', verbose_name='Users'),
        ),
    ]
