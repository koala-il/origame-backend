# Generated by Django 3.0.5 on 2020-04-21 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_imagefile_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='file',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.CreateModel(
            name='CustomerNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='crm.Customer')),
            ],
        ),
    ]
