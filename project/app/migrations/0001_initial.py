# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('app_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_dfields', self.gf('django_orm.postgresql.hstore.fields.DictionaryField')(db_index=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('app', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('app_person')


    models = {
        'app.person': {
            'Meta': {'object_name': 'Person'},
            '_dfields': ('django_orm.postgresql.hstore.fields.DictionaryField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']