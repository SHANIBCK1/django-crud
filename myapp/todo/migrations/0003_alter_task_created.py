# Generated by Django 4.1.6 on 2023-05-24 05:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_remove_task_deadline_alter_task_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="created",
            field=models.DateTimeField(default="2023-05-24 05:01"),
        ),
    ]
