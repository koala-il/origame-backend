# Generated by Django 3.0.5 on 2020-04-27 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_imagefile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_modify_date',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='customernote',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='customernote',
            old_name='last_modify_date',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='imagefile',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='imagefile',
            old_name='last_modify_date',
            new_name='modified_at',
        ),
    ]
