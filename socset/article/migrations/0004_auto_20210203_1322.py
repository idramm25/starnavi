# Generated by Django 3.1.6 on 2021-02-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210203_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Image',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
        migrations.DeleteModel(
            name='ArticleImage',
        ),
    ]
