from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class EvalWorkDetails(grok.GlobalUtility):
    grok.name('ilo.vocabulary.eval_work_details') 
    grok.implements(IVocabularyFactory)

    items = [
        (
         'Has worked with EVAL',
         u'Has worked with EVAL',
        ),
        (
         'Has alert status',
         u'Has alert status',
        ),
        (
         'Has contact eval status',
         u'Has contact eval status',
        ),
        ]

    def __call__(self, context):
        terms = [ SimpleTerm(value=pair[0], token=pair[0],
            title=pair[1]) for pair in self.items ]
        return SimpleVocabulary(terms)
