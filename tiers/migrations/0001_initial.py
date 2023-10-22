# Generated by Django 4.2.6 on 2023-10-21 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TierList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TierRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('order', models.PositiveSmallIntegerField()),
                ('tierlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='tiers.tierlist')),
            ],
        ),
        migrations.CreateModel(
            name='TierItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('image', models.ImageField(upload_to='items')),
                ('tierlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiers.tierlist')),
                ('tierrow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiers.tierrow')),
            ],
        ),
    ]
