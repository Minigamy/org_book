# Generated by Django 4.2.2 on 2023-07-03 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_alter_employee_orgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='orgid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guide.structure'),
        ),
    ]
