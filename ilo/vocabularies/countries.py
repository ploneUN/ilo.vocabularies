from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

VALUES=[
    'Afghanistan','Bangladesh', 'Bhutan','Brunei','Cambodia', 'China', 
    'Cook Islands', 'Democratic People\'s Republic of Korea', 
    'Federated States of Micronesia', 'Fiji', 'India', 'Indonesia', 
    'Iran', 'Japan', 'Kiribati', 'Lao PDR', 'Malaysia', 'Maldives', 
    'Marshall Islands', 'Mongolia', 'Myanmar', 'Nauru', 'Nepal', 'Niue',
    'Pakistan', 'Palau', 'Papua New Guinea', 'Philippines', 
    'Republic of Korea', 'Samoa','Singapore', 'Solomon Islands', 
    'Sri Lanka', 'Thailand', 'Timor-Leste', 'Tokelau', 'Tonga', 
    'Tuvalu', 'Vanuatu','Viet Nam','HQ','ITC Turin', 'Other Regions'
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(VALUES)

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='ilo.vocabulary.countries')
