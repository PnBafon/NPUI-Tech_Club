# Generated by Django 4.2.6 on 2023-10-25 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_applications_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='applicants',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='landing_page.applications'),
        ),
    ]
