# Generated by Django 3.0 on 2019-12-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funds', '0002_auto_20191212_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipagesmodel',
            name='fundFourURL',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='wikipagesmodel',
            name='fundOneURL',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='wikipagesmodel',
            name='fundThreeURL',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='wikipagesmodel',
            name='fundTwoURL',
            field=models.TextField(),
        ),
    ]