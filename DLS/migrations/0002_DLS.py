# Generated by Django 2.2.3 on 2019-08-07 07:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DLS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DLS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
