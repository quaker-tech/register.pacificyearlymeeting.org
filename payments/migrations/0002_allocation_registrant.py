# Generated by Django 2.2.9 on 2020-01-31 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='registrant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payment_allocations', to='registration.Registrant'),
        ),
    ]
