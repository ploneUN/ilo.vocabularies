from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource


class EvalThemes(grok.GlobalUtility):
    grok.name('ilo.vocabulary.evalthemes')
    grok.implements(IVocabularyFactory)

    _terms = [
        {
            'value': 'employment',
            'title': 'EMPLOYMENT',
            'token': 'employment',
        },
        {
            'value': 'social proctection',
            'title': 'SOCIAL PROTECTION',
            'token': 'social protection',
        },
        {
            'value': 'social dialogue',
            'title': 'SOCIAL DIALOGUE',
            'token': 'social dialogue',
            },
        {
            'value': 'work quality',
            'title': 'WORK QUALITY',
            'token': 'work quality',
        },
        {
            'value': 'enterprises',
            'title': 'ENTERPRISES',
            'token': 'enterprises',
        },
        {
            'value': 'sectors',
            'title': 'SECTORS',
            'token': 'sectors',
        },



    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
