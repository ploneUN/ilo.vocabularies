from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from Products.CMFCore.utils import getToolByName

themes = [
    'Child Labour',
    'Communications and Knowledge',
    'Decent Work',
    'Domestic Workers',
    'Economic and Social Development',
    'Employers\' Activities',
    'Employment Promotion',
    'Employment Security',
    'Equality and Discrimination',
    'Finance and Administrative Services',
    'Forced Labour',
    'Freedom of Association and The Right to Collective Bargaining',
    'Green Jobs',
    'HIV/AIDS',
    'Individual Sectors and Industries',
    'Industrial Relations',
    'IT Services',
    'Labour Law',
    'Labour Inspection and Administration',
    'Labour Migration',
    'Labour Standards',
    'Management Services',
    'Maritime Labour Convention',
    'Millennium Development Goals',
    'Programming, M&E',
    'Rural Development',
    'Safety and Health at Work',
    'Skills, Knowledge and Employability',
    'Social Security',
    'Tripartism and Social Dialogue',
    'Workers\' Activities',
    'Working Conditions',
    'Youth Employment',
    'Other',
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(themes)

grok.global_utility(VocabularyFactory, IVocabularyFactory, 
                    name='ilo.vocabulary.themes')
