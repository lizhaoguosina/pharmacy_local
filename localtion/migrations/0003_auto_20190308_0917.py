# Generated by Django 2.1.7 on 2019-03-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localtion', '0002_auto_20190308_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='te_id',
            field=models.CharField(max_length=256, verbose_name='固定资产编码'),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='ph_id',
            field=models.CharField(max_length=1024, verbose_name='药品编码'),
        ),
    ]