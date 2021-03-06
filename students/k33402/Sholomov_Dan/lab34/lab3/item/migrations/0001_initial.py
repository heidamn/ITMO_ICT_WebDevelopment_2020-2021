# Generated by Django 3.1.5 on 2021-01-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('type', models.CharField(choices=[('Запчасть', 'Запчасть'), ('Велосипед', 'Велосипед'), ('Одежда', 'Одежда')], default='Запчасть', max_length=14, verbose_name='Тип')),
                ('description', models.TextField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
