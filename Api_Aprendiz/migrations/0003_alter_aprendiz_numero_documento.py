# Generated by Django 4.2.4 on 2023-09-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_Aprendiz', '0002_aprendiz_numero_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprendiz',
            name='numero_documento',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
