# Generated by Django 3.2.4 on 2021-06-10 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email address')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField(verbose_name='Sum of a transaction')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money_planning.users')),
            ],
        ),
    ]
