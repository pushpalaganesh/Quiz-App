# Generated by Django 5.1.4 on 2024-12-10 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0003_rename_gfg_name_type_quiz_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='quiz_category',
            new_name='gfg_name',
        ),
    ]
