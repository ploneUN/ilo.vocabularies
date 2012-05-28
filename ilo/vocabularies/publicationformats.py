from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

VALUES=[
    'Print',
    'Web PDF',
    'CD ROM',
    'DVD',
    'VDO',
    'Other'
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(VALUES)

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='ilo.vocabulary.publicationformats')
