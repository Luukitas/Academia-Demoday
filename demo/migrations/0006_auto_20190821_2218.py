# Generated by Django 2.2.4 on 2019-08-22 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20190821_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='img_perfil',
            field=models.ImageField(blank=True, default='default/Empresa.jpg', null=True, upload_to='images/', verbose_name='Imagem'),
        ),
    ]
