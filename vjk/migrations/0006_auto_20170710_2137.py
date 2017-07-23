# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vjk', '0005_auto_20170710_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='province',
            field=models.CharField(blank=True, choices=[('NS', 'Nova Scotia'), ('YT', 'Yukon'), ('NU', 'Nunavut'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('ON', 'Ontario'), ('BC', 'British Columbia'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('NL', 'Newfoundland and Labrador'), ('SK', 'Saskatchewan'), ('AB', 'Alberta'), ('NT', 'Northwest Territories')], max_length=20, null=True, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='student',
            name='aboriginal_group',
            field=models.CharField(blank=True, choices=[('Metis', 'Metis'), ('First Nations', 'First Nations'), ('Inuit', 'Inuit')], max_length=20, null=True, verbose_name='Aboriginal Group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True, verbose_name='Guard. Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='province',
            field=models.CharField(blank=True, choices=[('NS', 'Nova Scotia'), ('YT', 'Yukon'), ('NU', 'Nunavut'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('ON', 'Ontario'), ('BC', 'British Columbia'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('NL', 'Newfoundland and Labrador'), ('SK', 'Saskatchewan'), ('AB', 'Alberta'), ('NT', 'Northwest Territories')], max_length=20, null=True, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='student',
            name='reference_province',
            field=models.CharField(blank=True, choices=[('NS', 'Nova Scotia'), ('YT', 'Yukon'), ('NU', 'Nunavut'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('ON', 'Ontario'), ('BC', 'British Columbia'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('NL', 'Newfoundland and Labrador'), ('SK', 'Saskatchewan'), ('AB', 'Alberta'), ('NT', 'Northwest Territories')], max_length=20, null=True, verbose_name='Ref. Province'),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher_email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True, verbose_name='Teach. Email'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='province',
            field=models.CharField(blank=True, choices=[('NS', 'Nova Scotia'), ('YT', 'Yukon'), ('NU', 'Nunavut'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('ON', 'Ontario'), ('BC', 'British Columbia'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('NL', 'Newfoundland and Labrador'), ('SK', 'Saskatchewan'), ('AB', 'Alberta'), ('NT', 'Northwest Territories')], max_length=20, null=True, verbose_name='Province'),
        ),
    ]
