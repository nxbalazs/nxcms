# Generated by Django 4.1.6 on 2023-04-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_pagesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesettings',
            name='menu1_text',
            field=models.CharField(default='Homepage', max_length=50),
        ),
        migrations.AddField(
            model_name='pagesettings',
            name='menu2_text',
            field=models.CharField(default='Blog', max_length=50),
        ),
        migrations.AddField(
            model_name='pagesettings',
            name='menu3_text',
            field=models.CharField(default='Links', max_length=50),
        ),
        migrations.AddField(
            model_name='pagesettings',
            name='menu4_text',
            field=models.CharField(default='Login', max_length=50),
        ),
        migrations.AddField(
            model_name='pagesettings',
            name='menu5_text',
            field=models.CharField(default='Logout', max_length=50),
        ),
        migrations.AddField(
            model_name='pagesettings',
            name='menu6_text',
            field=models.CharField(default='Dashboard', max_length=50),
        ),
    ]
