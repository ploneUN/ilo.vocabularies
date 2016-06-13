from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

VALUES=[
    'Afghanistan (The Islamic State of)','Albania','Algeria','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','the Bahamas','Bahrain','Bangladesh (The People\'s Republic of)','Barbados','Belarus','Belgium','Belize','Benin','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Bhutan','Brunei Darussalam','Bulgaria','Burkina Faso','Burundi','Cambodia (The Kingdom of)', 'Cameron','Canada','Cabo Verde','Chad','Chile','Colombia','the Comoros','the Congo','China (The People\' Republic of)', 'Cook Islands', 'Korea (The Republic of)','Costa Rica','Cote d Ivoire','Croatia','Cuba','Cyprus','Denmark','Djibouti','Dominica','Ecuador','Egypt','El Salvador','Equatorial Guinea', 'Eritrea','Estonia','Ethiopia','Fiji','Finand','Federated States of Micronesia', 'France','Gabon','the Gambia','Georgia','Germany','Ghana','Greece','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia', 'Iran (Islamic Republic of)','Iraq', 'Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Kuwait','Kyrgyzstan','Latvia', 'Lebanon','Lesotho','Liberia','Libya','Lithuania','Luxembourg','Lao People\'s Democratic Republic','Madagascar','Malawi','Malaysia', 'Maldives (The Republic of)', 'Mali','Malta','Marshall Islands','Mauritania','Mauritus','Mexico','Mongolia','Montenegro','Morocco','Myanmar','Mozambique','Namibia','Nauru', 'Nepal','New Zealand','the Netherlands','Niue','Nicaragua','the Niger','Nigeria','Norway','Oman','Pakistan', 'Palau (The Republic of)', 'Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Quatar','Romania','the Russian Federation','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines', 'Republic of Korea', 'Samoa','Singapore (The Republic of)', 'San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovenia','Solomon Islands', 'Somalia','South Africa','South Sudan','Spain','Sri Lanka','the Sudan', 'Suriname','Swaziland','Sweden','Switzerland','Tajikistan','Thailand (The Kingdom of)', 'Timor-Leste','Togo', 'Tokelau', 'Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu', 'Uganda','Ukraine','the United Kingdom','the United States','Uruguay','Uzbekistan','Vanuatu','Vanuatu','Viet Nam (The Socialist Republic of)','Yemen','Zambia','Zimbabwe',
    'HQ','ITC Turin', 'Other'
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(sorted(VALUES))

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='ilo.vocabulary.countries')
