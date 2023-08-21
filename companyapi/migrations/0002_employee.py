# Generated by Django 4.2.4 on 2023-08-13 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('about_me', models.TextField()),
                ('position', models.CharField(choices=[('TL', 'TL'), ('Manager', 'Manager'), ('HR', 'HR')], max_length=50)),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapi.company')),
            ],
        ),
    ]
