# Generated by Django 5.1 on 2024-08-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название курса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание курса')),
                ('imagery', models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='Изображение(превью)')),
            ],
            options={
                'verbose_name': 'Учебный курс',
                'verbose_name_plural': 'Учебные курсы',
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название лекции к теме')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание лекции')),
                ('imagery', models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='Изображение(превью)')),
                ('content', models.FileField(blank=True, null=True, upload_to='materials/', verbose_name='Содержание лекции')),
                ('video', models.URLField(blank=True, max_length=150, null=True, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Лекция',
                'verbose_name_plural': 'Лекции',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название темы курса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание темы')),
                ('imagery', models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='Изображение(превью)')),
            ],
            options={
                'verbose_name': 'Тема курса',
                'verbose_name_plural': 'Темы курса',
            },
        ),
    ]
