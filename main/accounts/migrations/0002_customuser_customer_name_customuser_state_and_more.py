# Generated by Django 4.1.3 on 2022-11-27 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='customer_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.CharField(default='Texas', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='street',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='town',
            field=models.CharField(default='Amarillo', max_length=20),
        ),
    ]