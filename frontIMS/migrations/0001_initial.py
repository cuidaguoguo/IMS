# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Couser',
            fields=[
                ('CouserId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('CouserName', models.CharField(max_length=20)),
                ('Period', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('GradeId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('GradeName', models.CharField(max_length=20)),
                ('GradeNum', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Institude',
            fields=[
                ('InstitudeId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('InstitudeName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('MajorId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('MajorName', models.CharField(max_length=20)),
                ('InstitudeId', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Institude')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('ScoreId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Score', models.CharField(max_length=20)),
                ('CouserId', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Couser')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('PassWord', models.CharField(max_length=20)),
                ('UserName', models.CharField(max_length=10)),
                ('GradeId', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Grade')),
                ('InstitudeId', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Institude')),
                ('MajorId', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Major')),
                ('StuTeacher', models.ManyToManyField(to='frontIMS.Couser')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('TeacherId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('PassWord', models.CharField(max_length=20)),
                ('UserName', models.CharField(max_length=10)),
                ('InstitudeId', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Institude')),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='StudentId',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Student'),
        ),
        migrations.AddField(
            model_name='grade',
            name='InstitudeId',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Institude'),
        ),
        migrations.AddField(
            model_name='grade',
            name='MajorId',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Major'),
        ),
        migrations.AddField(
            model_name='couser',
            name='TeacherId',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='frontIMS.Teacher'),
        ),
    ]