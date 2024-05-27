# Generated by Django 5.0.6 on 2024-05-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_senha_alter_usuario_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_usuario',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, verbose_name='CPF'),
        ),
    ]
