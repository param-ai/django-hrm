# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-06 15:47
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('num_of_days', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LeaveCategory',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_leave', models.CharField(max_length=20)),
                ('number_of_days', models.PositiveIntegerField(validators=[
                 django.core.validators.MaxValueValidator(9999999999)])),
            ],
            options={
                'verbose_name_plural': 'Leave Categories',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('total_leaves', models.PositiveIntegerField(validators=[
                 django.core.validators.MaxValueValidator(9999999999)])),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='leave_category',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='leave_tracker.LeaveCategory'),
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='usr',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='leave_tracker.UserProfile'),
        ),
    ]
