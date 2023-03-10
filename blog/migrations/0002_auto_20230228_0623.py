# Generated by Django 3.2.18 on 2023-02-28 06:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(validators=[django.core.validators.RegexValidator('^[a-zA-Z\\W]*$', 'Only alphabets and special characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\W]*$', 'Only alphabets and special characters are allowed.')]),
        ),
    ]
