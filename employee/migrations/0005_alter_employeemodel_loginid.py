# Generated by Django 3.2.12 on 2022-06-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employeemodel_loginid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='loginId',
            field=models.CharField(default=166019, editable=False, max_length=6, unique=True),
        ),
    ]
