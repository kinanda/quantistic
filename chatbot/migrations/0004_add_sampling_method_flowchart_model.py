# Generated by Django 3.2.7 on 2021-12-04 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_alter_flowchart_path_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamplingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('video', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SamplingFlowchart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('path', models.CharField(max_length=64, unique=True)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='samplingflowcharts', to='chatbot.method')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
