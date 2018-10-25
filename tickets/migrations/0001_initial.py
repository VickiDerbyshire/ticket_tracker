# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-25 02:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('comment', models.TextField()),
                ('comment_html', models.TextField(blank=True, editable=False)),
                ('action', models.CharField(choices=[('no_action', 'No Action'), ('split', 'Split'), ('closed', 'Closed'), ('reopened', 'Re-Opened')], default='no_action', max_length=20)),
                ('private', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.FollowUp')),
                ('submitted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('assigned', 'Assigned'), ('reopened', 'Reopened'), ('split', 'Closed - Split'), ('new', 'New'), ('closed', 'Closed'), ('duplicate', 'Closed - Duplicate'), ('accepted', 'Accepted')], default=True, max_length=20)),
                ('ticket_type', models.CharField(choices=[('feature', 'Feature Request'), ('bug', 'Bug Report')], default=True, max_length=10)),
                ('description', models.TextField()),
                ('description_html', models.TextField(blank=True, editable=False)),
                ('priority', models.IntegerField(choices=[(4, 'Low'), (3, 'Normal'), (1, 'Critical'), (5, 'Very Low'), (2, 'High')])),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('votes', models.IntegerField(default=0)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Application')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tickets', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
                ('submitted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submitted_tickets', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('all_tickets', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TicketDuplicate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original', to='tickets.Ticket')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='duplicate', to='tickets.Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='UserVoteLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='followup',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket'),
        ),
    ]
