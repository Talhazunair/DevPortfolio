# Generated by Django 5.0.3 on 2024-03-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_projects_demo_link_projects_github_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='demo_link',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='github_link',
            field=models.URLField(default=''),
        ),
    ]