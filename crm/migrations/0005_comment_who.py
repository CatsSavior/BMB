# Generated by Django 2.2.3 on 2019-08-16 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20190816_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='who',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Student'),
        ),
    ]
