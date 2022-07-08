# Generated by Django 4.0.6 on 2022-07-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, null=True)),
                ('option1', models.CharField(max_length=100, null=True)),
                ('option2', models.CharField(max_length=100, null=True)),
                ('option3', models.CharField(max_length=100, null=True)),
                ('option4', models.CharField(max_length=100, null=True)),
                ('answer', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
