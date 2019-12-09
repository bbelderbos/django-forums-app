# Generated by Django 2.2.8 on 2019-12-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0008_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.TextField(choices=[('N', 'NotProvided'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='N', max_length=1),
        ),
    ]
