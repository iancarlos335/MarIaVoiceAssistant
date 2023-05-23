# Generated by Django 4.2.1 on 2023-05-23 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IaAudioResponse',
            fields=[
                ('AudioId', models.AutoField(primary_key=True, serialize=False)),
                ('AudioBinaryContent', models.BinaryField()),
                ('AudioStringContent', models.CharField(default='', max_length=255)),
            ],
        ),
    ]