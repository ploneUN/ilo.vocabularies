from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from Products.CMFCore.utils import getToolByName

subject_expertise = [
    "Advocacy, Media, Television, Publishing",
    "Agricultural Specialist",
    "Child Labour ",
    "Development Economics",
    "Development Projects",
    "Disabilities, Disabled Workers",
    "Domestic Workers",
    "Economic Reconstruction",
    "Editing, Writing",
    "Education",
    "Employers",
    "Employment Creation",
    "Employment Policy",
    "Enterprise Development",
    "Environmental Specialist",
    "Evaluation Experience",
    "Evaluation Expert",
    "Financial Auditing",
    "Forced labour",
    "Gender Policy",
    "Government infrastructure, roads, utilities",
    "Green Jobs",
    "HIV/AIDS",
    "Health Services, Health Policy",
    "Human Rights",
    "Human trafficking",
    "Humanitarian Affairs And Conflict Resolution",
    "Impact Assessment",
    "Income Generation - Micro Enterprises",
    "Income Generation - Micro Credit",
    "Indigenous People",
    "Labour Administration",
    "Labour Inspection",
    "Labour Law, Legislative Policy",
    "Labour Relations",
    "Management Information Systems",
    "Micro-insurance",
    "Migration",
    "National Planning",
    "Occupational Safety And Health",
    "Organizational Development",
    "Organizational Experience - Government ",
    "Organizational Experience - International NGO",
    "Organizational Experience - Other",
    "Organizational Experience - UN",
    "Participatory Methods",
    "Poverty",
    "Productivity",
    "Project Design",
    "Project Management",
    "Psycho-Social Issues",
    "Public Sector - Government",
    "Public Sector - Health",
    "Public Sector - Infrastructure",
    "Crisis & Risk Assessment",
    "Skills Development",
    "Small Enterprise Development",
    "Social Dialogue",
    "Social Security",
    "Social Protection",
    "Statistical Analysis",
    "Strategic Planning",
    "Surveys",
    "Sustainable Enterprises",
    "Training Of Trainers",
    "Workers' Rights",
    "Youth, Adolescent Development",
]

class VocabularyFactory(object):
    def __call__(self, context):
        return SimpleVocabulary.fromValues(subject_expertise)

grok.global_utility(VocabularyFactory, IVocabularyFactory, 
                    name='ilo.vocabulary.subject_expertise')
