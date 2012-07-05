from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

VALUES=[
    'Book',
    'Report',
    'Working paper',
    'Discussion paper',
    'Other'
]

NONOFFICIALPUB_VALUES=[
    'Book',
    'Report',
    'Other'
]

WORKINGPAPERPUBTYPE_VALUES=[
    'Working paper',
    'Discussion paper',
    'Other'
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(sorted(VALUES))

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='ilo.vocabulary.publicationtypes')

class NonOfficialPubTypeVocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(NONOFFICIALPUB_VALUES)

grok.global_utility(NonOfficialPubTypeVocabularyFactory, IVocabularyFactory,
        name='ilo.vocabulary.publicationtypes.nonofficialpublication')



class WorkingPaperPubTypeVocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(WORKINGPAPERPUBTYPE_VALUES)

grok.global_utility(WorkingPaperPubTypeVocabularyFactory, IVocabularyFactory,
        name='ilo.vocabulary.publicationtypes.workingpaper')



