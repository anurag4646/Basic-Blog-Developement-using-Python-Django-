# Generated by Django 3.0.1 on 2019-12-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]