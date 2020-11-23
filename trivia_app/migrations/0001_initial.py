# Generated by Django 3.1.3 on 2020-11-23 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndianFlagcolor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_flag_color', to='trivia_app.person')),
            ],
        ),
        migrations.CreateModel(
            name='BestCrickter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_crickter', to='trivia_app.person')),
            ],
        ),
    ]
