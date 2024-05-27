# Generated by Django 5.0.6 on 2024-05-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default=1234567890, max_length=100, verbose_name='Senha'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=11, unique=True, verbose_name='Contato'),
        ),
    ]
