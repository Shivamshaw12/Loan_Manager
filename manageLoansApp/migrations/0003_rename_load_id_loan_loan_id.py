# Generated by Django 4.2.5 on 2023-09-27 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageLoansApp', '0002_alter_loan_load_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='load_id',
            new_name='loan_id',
        ),
    ]