# Generated by Django 2.1.5 on 2019-01-25 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0014_auto_20170307_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='phase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='oth.Phase'),
        ),
    ]
