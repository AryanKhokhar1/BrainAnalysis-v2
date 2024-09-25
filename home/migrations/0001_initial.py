# Generated by Django 5.0.3 on 2024-09-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('question_text', models.TextField()),
                ('keyed', models.BinaryField()),
                ('domain', models.CharField(max_length=10)),
                ('facet', models.IntegerField()),
            ],
        ),
    ]
