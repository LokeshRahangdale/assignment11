# Generated by Django 2.2.3 on 2019-11-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin_Log', '0003_auto_20191109_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MarchantModel',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Model',
            fields=[
                ('p_no', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50, unique=True)),
                ('p_price', models.FloatField()),
                ('p_quantity', models.IntegerField()),
            ],
        ),
    ]
