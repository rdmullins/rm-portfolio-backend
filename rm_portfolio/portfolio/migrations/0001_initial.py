# Generated by Django 4.1.3 on 2022-11-19 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stack', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('screenshot', models.URLField()),
                ('repository', models.URLField()),
                ('live_link', models.URLField()),
                ('description', models.TextField()),
                ('tech_stack', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tech_stack_used', to='portfolio.techstack')),
            ],
        ),
    ]
