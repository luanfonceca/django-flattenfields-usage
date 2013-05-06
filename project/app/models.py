from django.db import models
from hstore_flattenfields import models as hs_models

class Person(hs_models.HStoreModel):
    name = models.CharField(null=False, max_length=100)

    def __unicode__(self, *args, **kwargs):
        return u"#%s - %s" % (self.pk, self.name)
