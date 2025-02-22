# Generated by Django 4.1 on 2022-09-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "createSprintApp",
            "0002_sprint_is_sprint_complete_alter_sprint_end_date_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="sprint", old_name="created_date", new_name="created_Date",
        ),
        migrations.RenameField(
            model_name="sprint", old_name="end_date", new_name="end_Date",
        ),
        migrations.RenameField(
            model_name="sprint",
            old_name="is_sprint_complete",
            new_name="is_Sprint_Complete",
        ),
        migrations.RenameField(
            model_name="sprint", old_name="start_date", new_name="start_Date",
        ),
        migrations.RemoveField(model_name="sprint", name="sprint_goal",),
        migrations.RemoveField(model_name="sprint", name="sprint_name",),
        migrations.AddField(
            model_name="sprint",
            name="sprint_Goal",
            field=models.CharField(default="sprint goal", max_length=250),
        ),
        migrations.AddField(
            model_name="sprint",
            name="sprint_Name",
            field=models.CharField(default="sprint name", max_length=100),
        ),
    ]
