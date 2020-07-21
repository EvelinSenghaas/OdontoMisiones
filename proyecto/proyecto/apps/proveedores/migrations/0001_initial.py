# Generated by Django 2.0 on 2020-07-20 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametros', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalProveedor',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre (*)')),
                ('empresa', models.CharField(max_length=200, null=True, verbose_name='Empresa (*)')),
                ('telefono', models.IntegerField(default=False, verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='e-mail')),
                ('contacto', models.CharField(max_length=200, verbose_name='Nombre de Contacto (*)')),
                ('nota', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nota ')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('domicilio', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='parametros.Domicilio')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical proveedor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre (*)')),
                ('empresa', models.CharField(max_length=200, null=True, verbose_name='Empresa (*)')),
                ('telefono', models.IntegerField(default=False, verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='e-mail')),
                ('contacto', models.CharField(max_length=200, verbose_name='Nombre de Contacto (*)')),
                ('nota', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nota ')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('domicilio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parametros.Domicilio')),
            ],
        ),
    ]
