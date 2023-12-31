# Generated by Django 3.2 on 2023-07-19 17:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Spymain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField()),
                ('height_feet', models.SmallIntegerField(blank=True, null=True)),
                ('weight', models.SmallIntegerField(blank=True, null=True)),
                ('bodyshape', models.CharField(choices=[('Rectangle', 'Rectangle'), ('Inverted Triangle', 'Inverted Triangle'), ('Hourglass', 'Hourglass'), ('Pear', 'Pear'), ('Apple', 'Apple'), ('Potato', 'Potato'), ('Unidentified', 'Unidentified')], default='Unidentified', max_length=100)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Waiting for the one', 'Searching')], default='Single', max_length=100)),
                ('Profession', models.CharField(blank=True, max_length=200, null=True)),
                ('College', models.CharField(blank=True, max_length=200, null=True)),
                ('approx_followers', models.SmallIntegerField(blank=True, null=True)),
                ('Country', models.CharField(blank=True, default='India', max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('Rating', models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], default='G', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='model_assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('profile_photo', models.ImageField(upload_to='profilephoto/')),
                ('instagram', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('twitter', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('snapchat', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('youtube', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('facebook', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('MXtakatak', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('chingari', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('josh', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('moj', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('discord', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('telegram', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('reddit', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('unknown', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('unknown1', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('unknown2', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('unknown3', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('models_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spymain.model_info')),
            ],
        ),
    ]
