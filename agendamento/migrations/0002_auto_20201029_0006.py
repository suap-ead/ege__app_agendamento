# Generated by Django 3.1.2 on 2020-10-29 00:06

from django.db import migrations
import suap_ead.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='status',
            field=suap_ead.fields.StringField(choices=[('Solicitado', 'Solicitado'), ('Deferido', 'Deferido'), ('Indeferido', 'Indeferido'), ('Cancelado', 'Cancelado')], default='Solicitado', max_length=250, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='dia',
            field=suap_ead.fields.StringField(choices=[('0', 'Seg'), ('1', 'Ter'), ('2', 'Qua'), ('3', 'Qui'), ('4', 'Sex'), ('5', 'Sab'), ('6', 'Dom')], max_length=250, verbose_name='Dia da semana'),
        ),
    ]
