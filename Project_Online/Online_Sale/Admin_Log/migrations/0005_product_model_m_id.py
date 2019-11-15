# Generated by Django 2.2.3 on 2019-11-10 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Log', '0004_admin_log_marchantmodel_product_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='m_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Admin_Log.MarchantModel'),
            preserve_default=False,
        ),
    ]
