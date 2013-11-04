from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from Products.CMFCore.utils import getToolByName

offices = [
    'RO - Asia and the Pacific',
    'CO - Bangkok',
    'CO - Beijing',
    'CO - Colombo',
    'CO - Dhaka',
    'CO - Hanoi',
    'CO - Islamabad',
    'CO - Jakarta',
    'CO - Kathmandu',
    'CO - Manila',
    'CO - Suva',
    'DWT - New Delhi',
    'CO - New Delhi',
    'DWT - Bangkok',
    'ILO - Dili',
    'ILO - Kabul',
    'ILO - Phnom Penh',
    'ILO - Tokyo',
    'ILO - Vientiane',
    'ILO - Yangon',
    'HQ',
    'ITC Turin',
    'Other Regions',
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(offices)

grok.global_utility(VocabularyFactory, IVocabularyFactory, 
                    name='ilo.vocabulary.offices')
