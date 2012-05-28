from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from Products.CMFCore.utils import getToolByName

class VocabularyFactory(object):
    def __call__(self, context):
        portal_properties = getToolByName(context, 'portal_properties')
        offices = portal_properties.ilo_properties.getProperty('themesopts')
        return SimpleVocabulary.fromValues(offices)

grok.global_utility(VocabularyFactory, IVocabularyFactory, 
                    name='ilo.vocabulary.themes')
