import logging

from django.db.models import Model, PositiveIntegerField, QuerySet, Manager, Max

from isc_common.fields.related import ForeignKeyCascade, ForeignKeyProtect
from kaf_pas.kd.models.document_attributes import Document_attributes
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy

logger = logging.getLogger(__name__)


class Lotsman_document_attr_cross1QuerySet(QuerySet):
    def delete(self):
        return super().delete()

    def _position_in_document(self, **kwargs):
        position_in_document = kwargs.get('position_in_document')
        document = kwargs.get('document')
        if document != None:
            if position_in_document == None:
                position_in_document_dict = Lotsman_document_attr_cross.objects.filter(document=document).aggregate(Max('position_in_document'))
                position_in_document = position_in_document_dict.get('position_in_document__max')
                if position_in_document == None:
                    position_in_document = 1
                else:
                    position_in_document += 1
                kwargs.setdefault('position_in_document', position_in_document)
                return kwargs
            else:
                return kwargs
        else:
            return kwargs

    def create(self, **kwargs):
        return super().create(**self._position_in_document(**kwargs))

    def update(self, **kwargs):
        return super().create(**self._position_in_document(**kwargs))

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Lotsman_document_attr_cross1Manager(Manager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Lotsman_document_attr_cross1QuerySet(self.model, using=self._db)


class Lotsman_document_attr_cross(Model):
    document = ForeignKeyCascade(Lotsman_documents_hierarcy)
    attribute = ForeignKeyProtect(Document_attributes)
    position_in_document = PositiveIntegerField()

    objects = Lotsman_document_attr_cross1Manager()

    def __str__(self):
        return f"{self.id}, document: [{self.document}], attribute: [{self.attribute}], position_in_document: {self.position_in_document},"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
        unique_together = (('document', 'position_in_document'),)
