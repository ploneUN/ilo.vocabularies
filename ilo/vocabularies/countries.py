from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

VALUES=[
    'Afghanistan (The Islamic State of)','Bangladesh (The People\'s Republic of)',
    'Bhutan','Brunei Darussalam','Cambodia (The Kingdom of)', 
    'China (The People\' Republic of)', 
    'Cook Islands', 'Korea (The Republic of)', 
    'Federated States of Micronesia', 'Fiji', 'India', 'Indonesia', 
    'Iran (Islamic Republic of)', 'Japan', 'Kiribati', 
    'Lao People\'s Democratic Republic', 'Malaysia', 'Maldives (The Republic of)', 
    'Marshall Islands', 'Mongolia', 'Myanmar', 'Nauru', 'Nepal', 'Niue',
    'Pakistan', 'Palau (The Republic of)', 'Papua New Guinea', 'Philippines', 
    'Republic of Korea', 'Samoa','Singapore (The Republic of)', 'Solomon Islands', 
    'Sri Lanka', 'Thailand (The Kingdom of)', 'Timor-Leste', 'Tokelau', 'Tonga', 
    'Tuvalu', 'Vanuatu','Viet Nam (The Socialist Republic of)',
    'HQ','ITC Turin', 'Other Regions'
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(sorted(VALUES))

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='ilo.vocabulary.countries')
