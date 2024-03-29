# Generated by Django 3.2.7 on 2021-12-04 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_add_sampling_method_flowchart_model'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_add_project_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamplingProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('progress', models.IntegerField(default=0)),
                ('flowchart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='chatbot.samplingflowchart')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
