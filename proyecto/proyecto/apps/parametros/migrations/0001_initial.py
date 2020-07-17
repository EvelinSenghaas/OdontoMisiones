# Generated by Django 2.0 on 2020-07-17 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('barrio', models.CharField(max_length=50, verbose_name='Barrio')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100, verbose_name='Calle')),
                ('nro', models.CharField(max_length=50, verbose_name='Numero')),
                ('mz', models.CharField(blank=True, max_length=50, null=True, verbose_name='Manzana')),
                ('departamento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Departamento')),
                ('piso', models.CharField(blank=True, max_length=50, null=True, verbose_name='Piso')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parametros.Barrio')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalBarrio',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('barrio', models.CharField(max_length=50, verbose_name='Barrio')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical barrio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLocalidad',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical localidad',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProvincia',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('provincia', models.CharField(max_length=50, verbose_name='Provincia')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical provincia',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('provincia', models.CharField(max_length=50, verbose_name='Provincia')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parametros.Provincia'),
        ),
        migrations.AddField(
            model_name='historicallocalidad',
            name='provincia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='parametros.Provincia'),
        ),
        migrations.AddField(
            model_name='historicalbarrio',
            name='localidad',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='parametros.Localidad'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parametros.Localidad'),
        ),
    ]
