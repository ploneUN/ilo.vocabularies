from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from Products.CMFCore.utils import getToolByName

subject_expertise = [
    "Advocacy, media, television, publishing",
    "Agricultural specialist",
    "Child Labour ",
    "Development economics",
    "Development projects",
    "Disabilities, disabled workers",
    "Domestic workers",
    "Economic reconstruction",
    "Editing, writing",
    "Education",
    "Employers",
    "Employment creation",
    "Employment policy",
    "Enterprise development",
    "Environmental specialist",
    "Evaluation Experience",
    "Evaluation Expert",
    "Financial Auditing",
    "Gender policy",
    "Green Jobs",
    "HIV/AIDS",
    "Health Services, Health Policy",
    "Human rights",
    "Humanitarian affairs and conflict resolution",
    "Impact Assessment",
    "Indigenous people",
    "Labour administration",
    "Labour inspection",
    "Labour Law, Legislative Policy",
    "Labour relations",
    "Management information systems",
    "Micro-credit",
    "Migration",
    "Occupational safety and health",
    "Organizational development",
    "Organizational experience - Government ",
    "Organizational experience -  International  NGO",
    "Organizational experience - Other",
    "Organizational experience - UN",
    "Poverty",
    "Project design",
    "Project management",
    "Psycho-social issues",
    "Public sector - Government",
    "Public sector - Health",
    "Public sector - Infrastructure",
    "Crisis & Risk Assessment",
    "Skills development",
    "Small enterprise development",
    "Social Dialogue",
    "Social Security",
    "Social Protection",
    "Statistical Analysis",
    "Strategic planning",
    "Surveys",
    "Sustainable enterprises",
    "Training of Trainers",
    "Workers' rights",
    "Youth, adolescent development",
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(subject_expertise)

grok.global_utility(VocabularyFactory, IVocabularyFactory, 
                    name='ilo.vocabulary.subject_expertise')
