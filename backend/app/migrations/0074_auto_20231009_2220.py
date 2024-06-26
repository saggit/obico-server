# Generated by Django 3.2.22 on 2023-10-09 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_auto_20230128_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='gcodefile',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='octoprinttunnel',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='print',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='printer',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='gcodefile',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='octoprinttunnel',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='print',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
