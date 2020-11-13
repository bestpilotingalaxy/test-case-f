# Generated by Django 3.1.3 on 2020-11-13 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_variant_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='poll',
        ),
        migrations.AlterField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.poll', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='polls.question', verbose_name='Вопрос'),
        ),
    ]
