# Generated by Django 5.0.4 on 2024-05-27 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_position_employees_count_alter_user_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='payout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonuses', to='users.payouts'),
        ),
        migrations.AlterField(
            model_name='payouts',
            name='begin_date_interval',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='payouts',
            name='end_date_interval',
            field=models.DateField(blank=True),
        ),
    ]
