# Generated by Django 5.0.6 on 2024-06-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact_module", "0003_alter_contactus_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactus",
            name="phone",
            field=models.CharField(max_length=13, verbose_name="شماره تماس"),
        ),
    ]
