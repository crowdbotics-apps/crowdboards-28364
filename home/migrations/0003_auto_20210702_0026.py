# Generated by Django 2.2.20 on 2021-07-02 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_applications_plans_subscriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Subscriptions'),
        ),
    ]