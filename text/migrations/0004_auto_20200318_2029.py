# Generated by Django 3.0.3 on 2020-03-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0003_auto_20200318_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neuralnetwork',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]