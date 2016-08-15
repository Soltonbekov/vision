# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('income', '0002_auto_20160815_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('destination', models.CharField(default='Bills', max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('period', models.CharField(default='Monthly', max_length=100)),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0439 \u0440\u0430\u0441\u0445\u043e\u0434',
                'verbose_name_plural': '\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u044b',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
                ('value_date', models.DateTimeField(auto_now_add=True)),
                ('drcr_ind', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': '\u043f\u0440\u043e\u0432\u043e\u0434\u043a\u0430',
                'verbose_name_plural': '\u043f\u0440\u043e\u0432\u043e\u0434\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Wallets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=3)),
                ('available_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u043a\u043e\u0448\u0435\u043b\u0435\u043a',
                'verbose_name_plural': '\u043a\u043e\u0448\u0435\u043b\u044c\u043a\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name': '\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0439 \u0434\u043e\u0445\u043e\u0434', 'verbose_name_plural': '\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u0434\u043e\u0445\u043e\u0434\u044b'},
        ),
        migrations.AddField(
            model_name='transactions',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income.Wallets'),
        ),
    ]