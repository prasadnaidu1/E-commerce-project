# Generated by Django 2.1.5 on 2019-01-10 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_loginimage_registerdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('p_id', models.IntegerField()),
            ],
        ),
    ]
