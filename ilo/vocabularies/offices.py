from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from Products.CMFCore.utils import getToolByName

offices = [
    'RO - Asia and the Pacific',
    'RO - Africa',
    'RO - Latin America and the Caribbean',
    'RO - Arab States',
    'RO – Europe and Central Asia',
    'CO - Abidjan',
    'CO - Abuja',
    'CO - Addis Ababa',
    'CO - Algiers',
    'CO - Antananarivo',
    'CO - Dar es Salaam',
    'CO - Harare',
    'CO - Kinshasa',
    'CO - Lusaka',
    'DWT – Cairo',
    'CO – Cairo',
    'DWT – Dakar',
    'CO – Dakar',
    'DWT – Pretoria',
    'CO – Pretoria',
    'DWT – Yaounde',
    'CO – Yaounde',
    'CO - Brasilia',
    'CO - Buenos Aires',
    'CO - Mexico',
    'DWT – Lima',
    'CO – Lima',
    'DWT – Port of Spain',
    'CO – Port of Spain',
    'DWT – San Jose',
    'CO – San Jose',
    'DWT – Santiago',
    'CO – Santiago',
    'ILO - CINTERFOR',
    'DWT – Beirut',
    'ILO - Representative',
    'ILO - Jerusalem',
    'ILO - Kuwait',
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
    'DWT – Budapest',
    'CO – Budapest',
    'DWT – Moscow',
    'CO – Moscow',
    'ILO – Ankara',
    'ILO – Berlin',
    'ILO – Brussels',
    'ILO – Lisbon',
    'ILO – Madrid',
    'ILO – Paris',
    'ILO – Rome',
    'NC – Astana',
    'NC – Baku',
    'NC – Belgrade',
    'NC – Bishkek',
    'NC – Chisinau',
    'NC – Dushanbe',
    'NC – Kiev',
    'NC – Minsk',
    'NC – Sarajevo',
    'NC – Skopje',
    'NC – Tirana',
    'NC – Yerevan',
    'HQ',
    'ITC Turin',
    'Other Regions',
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(offices)

grok.global_utility(VocabularyFactory, IVocabularyFactory, 
                    name='ilo.vocabulary.offices')
