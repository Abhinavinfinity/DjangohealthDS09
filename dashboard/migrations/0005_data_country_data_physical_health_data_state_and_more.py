# Generated by Django 4.1.4 on 2023-01-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_data_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='physical_health',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='student',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='tech_company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
