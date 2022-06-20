# Generated by Django 3.2.12 on 2022-06-18 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20220618_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='FertilizerStockDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.CharField(choices=[('p1', 'p1'), ('p2', 'p2'), ('p3', 'p3'), ('p4', 'p4'), ('p5', 'p5')], max_length=3)),
                ('date', models.DateField(default=datetime.date(2022, 6, 18))),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='loginId',
            field=models.CharField(default=960595, editable=False, max_length=6, unique=True),
        ),
    ]
