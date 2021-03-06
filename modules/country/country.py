#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields

__all__ = ['Country', 'Subdivision']


class Country(ModelSQL, ModelView):
    'Country'
    __name__ = 'country.country'
    name = fields.Char('Name', required=True, translate=True,
           help='The full name of the country.', select=True)
    code = fields.Char('Code', size=2, select=True,
           help='The ISO country code in two chars.\n'
           'You can use this field for quick search.', required=True)
    subdivisions = fields.One2Many('country.subdivision',
            'country', 'Subdivisions')

    @classmethod
    def __setup__(cls):
        super(Country, cls).__setup__()
        cls._sql_constraints += [
            ('name_uniq', 'UNIQUE(name)',
                'The name of the country must be unique.'),
            ('code_uniq', 'UNIQUE(code)',
                'The code of the country must be unique.'),
            ]
        cls._order.insert(0, ('name', 'ASC'))

    @classmethod
    def search_rec_name(cls, name, clause):
        if cls.search([('code',) + clause[1:]], limit=1):
            return [('code',) + clause[1:]]
        return [(cls._rec_name,) + clause[1:]]

    @classmethod
    def create(cls, vlist):
        vlist = [x.copy() for x in vlist]
        for vals in vlist:
            if 'code' in vals and vals['code']:
                vals['code'] = vals['code'].upper()
        return super(Country, cls).create(vlist)

    @classmethod
    def write(cls, countries, vals):
        if 'code' in vals and vals['code']:
            vals = vals.copy()
            vals['code'] = vals['code'].upper()
        super(Country, cls).write(countries, vals)


class Subdivision(ModelSQL, ModelView):
    "Subdivision"
    __name__ = 'country.subdivision'
    country = fields.Many2One('country.country', 'Country',
            required=True, select=True)
    name = fields.Char('Name', required=True, select=True, translate=True)
    code = fields.Char('Code', required=True, select=True)
    type = fields.Selection([
        ('administration', 'Administration'),
        ('administrative area', 'Administrative area'),
        ('administrative atoll', 'Administrative atoll'),
        ('administrative region', 'Administrative Region'),
        ('administrative territory', 'Administrative Territory'),
        ('area', 'Area'),
        ('atoll', 'Atoll'),
        ('arctic region', 'Arctic Region'),
        ('autonomous city', 'Autonomous City'),
        ('autonomous commune', 'Autonomous Commune'),
        ('autonomous communities', 'Autonomous communities'),
        ('autonomous community', 'Autonomous community'),
        ('autonomous district', 'Autonomous District'),
        ('autonomous island', 'Autonomous island'),
        ('autonomous monastic state', 'Autonomous monastic state'),
        ('autonomous municipality', 'Autonomous municipality'),
        ('autonomous province', 'Autonomous Province'),
        ('autonomous region', 'Autonomous Region'),
        ('autonomous republic', 'Autonomous republic'),
        ('autonomous sector', 'Autonomous sector'),
        ('autonomous territory', 'Autonomous territory'),
        ('autonomous territorial unit', 'Autonomous territorial unit'),
        ('borough', 'Borough'),
        ('canton', 'Canton'),
        ('capital city', 'Capital city'),
        ('capital district', 'Capital District'),
        ('capital metropolitan city', 'Capital Metropolitan City'),
        ('capital territory', 'Capital Territory'),
        ('chains (of islands)', 'Chains (of islands)'),
        ('city', 'City'),
        ('city corporation', 'City corporation'),
        ('city with county rights', 'City with county rights'),
        ('commune', 'Commune'),
        ('constitutional province', 'Constitutional province'),
        ('council area', 'Council area'),
        ('country', 'Country'),
        ('county', 'County'),
        ('department', 'Department'),
        ('dependency', 'Dependency'),
        ('development region', 'Development region'),
        ('district', 'District'),
        ('district council area', 'District council area'),
        ('division', 'Division'),
        ('economic prefecture', 'Economic Prefecture'),
        ('economic region', 'Economic region'),
        ('emirate', 'Emirate'),
        ('entity', 'Entity'),
        ('federal dependency', 'Federal Dependency'),
        ('federal district', 'Federal District'),
        ('federal territories', 'Federal Territories'),
        ('geographical entity', 'Geographical entity'),
        ('geographical region', 'Geographical region'),
        ('geographical unit', 'Geographical unit'),
        ('governorate', 'Governorate'),
        ('included for completeness', 'Included for completeness'),
        ('indigenous region', 'Indigenous region'),
        ('island', 'Island'),
        ('island council', 'Island council'),
        ('island group', 'Island group'),
        ('local council', 'Local council'),
        ('london borough', 'London borough'),
        ('metropolitan cities', 'Metropolitan cities'),
        ('metropolitan department', 'Metropolitan department'),
        ('metropolitan district', 'Metropolitan district'),
        ('metropolitan region', 'Metropolitan region'),
        ('municipalities', 'Municipalities'),
        ('municipality', 'Municipality'),
        ('oblast', 'Oblast'),
        ('outlying area', 'Outlying area'),
        ('overseas region/department', 'Overseas region/department'),
        ('overseas territorial collectivity',
            'Overseas territorial collectivity'),
        ('parish', 'Parish'),
        ('popularates', 'Popularates'),
        ('prefecture', 'Prefecture'),
        ('principality', 'Principality'),
        ('province', 'Province'),
        ('quarter', 'Quarter'),
        ('rayon', 'Rayon'),
        ('region', 'Region'),
        ('regional council', 'Regional council'),
        ('republic', 'Republic'),
        ('republican city', 'Republican City'),
        ('self-governed part', 'Self-governed part'),
        ('special administrative region', 'Special administrative region'),
        ('special city', 'Special city'),
        ('special district', 'Special District'),
        ('special island authority', 'Special island authority'),
        ('special municipality', 'Special Municipality'),
        ('special region', 'Special Region'),
        ('special zone', 'Special zone'),
        ('state', 'State'),
        ('territorial unit', 'Territorial unit'),
        ('territory', 'Territory'),
        ('town council', 'Town council'),
        ('two-tier county', 'Two-tier county'),
        ('union territory', 'Union territory'),
        ('unitary authority', 'Unitary authority'),
        ('unitary authority (england)', 'Unitary authority (england)'),
        ('unitary authority (wales)', 'Unitary authority (wales)'),
        ('zone', 'zone'),
        ], 'Type', required=True)
    parent = fields.Many2One('country.subdivision', 'Parent')

    @classmethod
    def __setup__(cls):
        super(Subdivision, cls).__setup__()
        cls._order.insert(0, ('code', 'ASC'))

    @classmethod
    def search_rec_name(cls, name, clause):
        if cls.search([('code',) + clause[1:]], limit=1):
            return [('code',) + clause[1:]]
        return [(cls._rec_name,) + clause[1:]]

    @classmethod
    def create(cls, vlist):
        vlist = [x.copy() for x in vlist]
        for vals in vlist:
            if 'code' in vals and vals['code']:
                vals['code'] = vals['code'].upper()
        return super(Subdivision, cls).create(vlist)

    @classmethod
    def write(cls, subdivisions, vals):
        if 'code' in vals and vals['code']:
            vals['code'] = vals['code'].upper()
        super(Subdivision, cls).write(subdivisions, vals)
