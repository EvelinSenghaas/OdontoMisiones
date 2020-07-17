# Generated by Django 2.0 on 2020-07-17 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0001_initial'),
        ('clientes', '0001_initial'),
        ('equipos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha (*)')),
                ('total', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total (*)')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cant', models.IntegerField(verbose_name='Cantidad (*) ')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Precio (*)')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cant', models.IntegerField(verbose_name='Cantidad (*) ')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Precio (*)')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalInsumo',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('marca', models.CharField(max_length=200, verbose_name='Marca (*)')),
                ('modelo', models.CharField(max_length=200, verbose_name='Modelo (*)')),
                ('fechaGarantia', models.DateField(verbose_name='Fecha de Garantia (*)')),
                ('numSerie', models.CharField(max_length=200, verbose_name='Numero de Serie (*)')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Precio (*)')),
                ('disponibilidad', models.IntegerField(verbose_name='Disponibilidad ')),
                ('nota', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nota')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('estado', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='equipos.Estado')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('proveedor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='proveedores.Proveedor')),
            ],
            options={
                'verbose_name': 'historical insumo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=200, verbose_name='Marca (*)')),
                ('modelo', models.CharField(max_length=200, verbose_name='Modelo (*)')),
                ('fechaGarantia', models.DateField(verbose_name='Fecha de Garantia (*)')),
                ('numSerie', models.CharField(max_length=200, verbose_name='Numero de Serie (*)')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Precio (*)')),
                ('disponibilidad', models.IntegerField(verbose_name='Disponibilidad ')),
                ('nota', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nota')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipos.Estado')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedores.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha (*)')),
                ('total', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Total (*)')),
                ('pago', models.BooleanField(default=False, verbose_name='Pago (*)')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente')),
                ('detalle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='insumos.DetalleVenta')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='insumos.Insumo'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='insumos.Insumo'),
        ),
        migrations.AddField(
            model_name='compra',
            name='detalle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='insumos.DetalleCompra'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedores.Proveedor'),
        ),
    ]
