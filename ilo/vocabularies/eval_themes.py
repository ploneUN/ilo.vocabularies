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
            'value': 'Employment',
            'title': 'EMPLOYMENT',
            'token': 'Employment',
        },
        {
            'value': 'Governance',
            'title': 'GOVERNANCE',
            'token': 'Governance',
        },
        {
            'value': 'Social proctection',
            'title': 'SOCIAL PROTECTION',
            'token': 'Social protection',
        },
        {
            'value': 'Social dialogue',
            'title': 'SOCIAL DIALOGUE',
            'token': 'Social dialogue',
            },
        {
            'value': 'Work quality',
            'title': 'WORK QUALITY',
            'token': 'Work quality',
        },
        {
            'value': 'Enterprises',
            'title': 'ENTERPRISES',
            'token': 'Enterprises',
        },
        {
            'value': 'Sectors',
            'title': 'SECTORS',
            'token': 'Sectors',
        },



    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
