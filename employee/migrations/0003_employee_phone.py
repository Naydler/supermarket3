# Generated by Django 5.1.2 on 2024-10-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_privilege'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
