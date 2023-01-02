# Generated by Django 4.1.3 on 2023-01-02 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_aipost_answer_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aipost',
            name='answer',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aipost')),
            ],
        ),
    ]