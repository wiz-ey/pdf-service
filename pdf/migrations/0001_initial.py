# Generated by Django 4.0 on 2021-12-12 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SessionFileLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pdf.filelink')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('input_files', models.ManyToManyField(through='pdf.SessionFileLink', to='pdf.FileLink')),
                ('output_file', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_session', to='pdf.filelink')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sessionfilelink',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf.usersession'),
        ),
    ]