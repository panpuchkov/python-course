# Generated by Django 3.0.6 on 2020-05-27 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ProductProp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPropsValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(max_length=1024)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Product')),
                ('productPropsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.ProductProp')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Product')),
            ],
            options={
                'verbose_name_plural': 'goods',
            },
        ),
    ]
