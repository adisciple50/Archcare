# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgressReport',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('content_of_one_to_one_support', models.TextField(verbose_name='Content of 1-1 Support')),
                ('evaluation_and_comments', models.TextField(verbose_name='Evaluation & Comments')),
                ('date_and_time_signed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=5, choices=[('MR', 'Mr'), ('MISS', 'Miss'), ('MRS', 'Mrs'), ('MS', 'Ms'), ('DR', 'Dr'), ('PROF', 'Prof.'), ('REVD', 'Revd')], verbose_name='Title')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=255, verbose_name='Surname')),
                ('full_name', models.CharField(max_length=518, verbose_name='Full Name')),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=5, choices=[('MR', 'Mr'), ('MISS', 'Miss'), ('MRS', 'Mrs'), ('MS', 'Ms'), ('DR', 'Dr'), ('PROF', 'Prof.'), ('REVD', 'Revd')], verbose_name='Title')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=255, verbose_name='Surname')),
                ('full_name', models.CharField(max_length=518, verbose_name='Full Name')),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyReport',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('morning', models.TextField(verbose_name='morning')),
                ('evening', models.TextField(verbose_name='evening')),
                ('daily_total_one_to_one_support_hours_provided', models.DecimalField(decimal_places=2, max_digits=5)),
                ('service_user', models.ForeignKey(to='ArchForms.ServiceUser')),
            ],
        ),
    ]
