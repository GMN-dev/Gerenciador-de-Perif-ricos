# Generated by Django 4.0.5 on 2022-06-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peripheral_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastroproduto',
            name='tipo',
            field=models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saida')], default='Entrada', max_length=250),
        ),
    ]