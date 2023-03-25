# Generated by Django 4.1.7 on 2023-03-25 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_autor_alter_libro_options_libro_isbn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Editorial')),
                ('telefono', models.CharField(max_length=15, null=True, unique=True, verbose_name='teléfono')),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editorales',
            },
        ),
    ]