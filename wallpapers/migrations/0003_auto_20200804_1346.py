# Generated by Django 3.0.9 on 2020-08-04 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallpapers', '0002_auto_20200804_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Wildlife', max_length=30),
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallpapers.category'),
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallpapers.location'),
        ),
    ]