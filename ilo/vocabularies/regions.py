from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

VALUES=[
    'HQ',
    'Asia',
    'Africa',
    'Americas',
    'Arab States',
    'Europe',
]

class VocabularyFactory(object):
    def __call__(self, context):
        
        VALUES.sort()
        terms = [SimpleTerm(value=pair, token=pair, title=pair) for pair in VALUES]
        return SimpleVocabulary(terms)

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='ilo.vocabulary.regions')
