# Generated by Django 4.2.11 on 2024-06-15 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='method_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='payment_api.method'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
