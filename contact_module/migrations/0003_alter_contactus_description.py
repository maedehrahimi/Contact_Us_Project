# Generated by Django 5.0.6 on 2024-06-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact_module", "0002_alter_contactus_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactus",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="پاسخ تماس با ما"
            ),
        ),
    ]
