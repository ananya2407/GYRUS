# Generated by Django 3.0.2 on 2020-01-21 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfUsers', models.IntegerField(blank=True, default=0)),
                ('authUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('clumpThickness', models.FloatField()),
                ('uniformityCellSize', models.FloatField()),
                ('uniformityCellShape', models.FloatField()),
                ('marginalAdhesion', models.FloatField()),
                ('singleEpithelialCellSize', models.FloatField()),
                ('bareNuclei', models.FloatField()),
                ('blandChromatin', models.FloatField()),
                ('normalNucleoli', models.FloatField()),
                ('mitoses', models.FloatField()),
                ('empUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('senior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loginsignup.Authority')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('lastDate', models.DateField()),
                ('completedDate', models.DateField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('auth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loginsignup.Authority')),
                ('emp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loginsignup.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('auth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loginsignup.Authority')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
