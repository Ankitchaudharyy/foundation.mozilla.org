# Generated by Django 2.2.16 on 2020-11-26 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0001_to_0026"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="internet_health_issues",
        ),
        migrations.DeleteModel(
            name="Affiliation",
        ),
        migrations.DeleteModel(
            name="InternetHealthIssue",
        ),
        migrations.DeleteModel(
            name="Person",
        ),
    ]
