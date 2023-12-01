# Generated by Django 4.2.7 on 2023-11-30 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0004_remove_pessoa_cargo_pessoa_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('descricao', models.TextField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.pessoa')),
            ],
        ),
    ]