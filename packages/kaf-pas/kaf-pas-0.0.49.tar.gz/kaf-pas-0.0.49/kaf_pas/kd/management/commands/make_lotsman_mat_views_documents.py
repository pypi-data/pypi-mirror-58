import logging

from django.conf import settings
from django.core.management import BaseCommand
from django.db import connection
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcyManager
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError

from kaf_pas.system.models.contants import Contants
from one_c.models.entities import Entities, Field
from one_c.models.entity_1c import Entity_1c
from one_c.models.one_c_params_entity_view import One_c_params_entity_view

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            Lotsman_documents_hierarcyManager.make_mview()


        except Exception as ex:
            raise ex
