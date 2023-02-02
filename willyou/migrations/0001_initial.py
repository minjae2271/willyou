# Generated by Django 4.1.6 on 2023-02-02 13:32

from django.db import migrations, models
import django.db.models.deletion
import willyou.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Couple',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('groom', models.CharField(max_length=10)),
                ('bride', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('groom_phone', models.CharField(max_length=11)),
                ('bride_phone', models.CharField(max_length=11)),
                ('groom_father_name', models.CharField(max_length=10)),
                ('groom_mother_name', models.CharField(max_length=10)),
                ('bride_father_name', models.CharField(max_length=10)),
                ('bride_mother_name', models.CharField(max_length=10)),
                ('groom_father_phone', models.CharField(max_length=11)),
                ('groom_mother_phone', models.CharField(max_length=11)),
                ('bride_father_phone', models.CharField(max_length=11)),
                ('bride_mother_phone', models.CharField(max_length=11)),
                ('groom_bank', models.CharField(max_length=10)),
                ('groom_account', models.CharField(max_length=14)),
                ('bride_bank', models.CharField(max_length=10)),
                ('bride_account', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='WeddingImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=willyou.models.image_upload_path)),
                ('couple', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='willyou.couple')),
            ],
        ),
    ]
