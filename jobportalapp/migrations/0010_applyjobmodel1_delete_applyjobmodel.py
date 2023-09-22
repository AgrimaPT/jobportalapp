# Generated by Django 4.2.2 on 2023-08-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0009_remove_applyjobmodel_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyjobmodel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn', models.CharField(max_length=20)),
                ('dsg', models.CharField(max_length=20)),
                ('nm', models.CharField(max_length=20)),
                ('eml', models.EmailField(max_length=254)),
                ('qlfn', models.CharField(max_length=20)),
                ('phno', models.CharField(max_length=20)),
                ('ex', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('>5', '>5')], max_length=20)),
                ('cv', models.FileField(upload_to='jobportalapp/static')),
            ],
        ),
        migrations.DeleteModel(
            name='applyjobmodel',
        ),
    ]
