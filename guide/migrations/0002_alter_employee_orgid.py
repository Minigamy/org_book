# Generated by Django 4.2.2 on 2023-07-03 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='orgid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='guide.structure'),
        ),
    ]