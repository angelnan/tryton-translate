#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
import vobject

from trytond.tools import reduce_ids
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta


__all__ = ['Event']
__metaclass__ = PoolMeta


class Event:
    __name__ = 'calendar.event'

    @classmethod
    def __setup__(cls):
        super(Event, cls).__setup__()
        cls._error_messages.update({
            'transparent': 'Free',
            'opaque': 'Busy',
            })

    @classmethod
    def search(cls, domain, offset=0, limit=None, order=None, count=False,
            query_string=False):
        if Transaction().user:
            domain = domain[:]
            domain = [domain,
                ['OR',
                    [
                        ('classification', '=', 'confidential'),
                        ['OR',
                            ('calendar.owner', '=', Transaction().user),
                            ('calendar.write_users', '=', Transaction().user),
                            ],
                        ],
                    ('classification', '!=', 'confidential'),
                    ],
                ]
        return super(Event, cls).search(domain, offset=offset, limit=limit,
            order=order, count=count, query_string=query_string)

    @classmethod
    def create(cls, vlist):
        events = super(Event, cls).create(vlist)
        if (cls.search([('id', 'in', [x.id for x in events])], count=True)
                != len(events)):
            cls.raise_user_error('access_error', cls.__doc__)
        return events

    @classmethod
    def _clean_private(cls, record, transp):
        '''
        Clean private record
        '''
        summary = cls.raise_user_error(transp, raise_exception=False)
        if 'summary' in record:
            record['summary'] = summary

        vevent = None
        if 'vevent' in record:
            vevent = record['vevent']
            if vevent:
                vevent = vobject.readOne(str(vevent))
                if hasattr(vevent, 'summary'):
                    vevent.summary.value = summary

        for field, value in (
                ('description', ''),
                ('categories', []),
                ('location', None),
                ('status', ''),
                ('organizer', ''),
                ('attendees', []),
                ('alarms', [])):
            if field in record:
                record[field] = value
            if field + '.rec_name' in record:
                record[field + '.rec_name'] = ''
            if vevent:
                if hasattr(vevent, field):
                    delattr(vevent, field)
        if vevent:
            record['vevent'] = vevent.serialize()

    @classmethod
    def read(cls, ids, fields_names=None):
        Rule = Pool().get('ir.rule')
        cursor = Transaction().cursor
        if len(set(ids)) != cls.search([('id', 'in', ids)],
                count=True):
            cls.raise_user_error('access_error', cls.__doc__)

        writable_ids = []
        domain1, domain2 = Rule.domain_get(cls.__name__, mode='write')
        if domain1:
            for i in range(0, len(ids), cursor.IN_MAX):
                sub_ids = ids[i:i + cursor.IN_MAX]
                red_sql, red_ids = reduce_ids('id', sub_ids)
                cursor.execute('SELECT id FROM "' + cls._table + '" '
                    'WHERE ' + red_sql + ' AND (' + domain1 + ')',
                    red_ids + domain2)
                writable_ids.extend(x[0] for x in cursor.fetchall())
        else:
            writable_ids = ids
        writable_ids = set(writable_ids)

        if fields_names is None:
            fields_names = []
        fields_names = fields_names[:]
        to_remove = set()
        for field in ('classification', 'calendar', 'transp'):
            if field not in fields_names:
                fields_names.append(field)
                to_remove.add(field)
        res = super(Event, cls).read(ids, fields_names=fields_names)
        for record in res:
            if record['classification'] == 'private' \
                    and record['id'] not in writable_ids:
                cls._clean_private(record, record['transp'])
            for field in to_remove:
                del record[field]
        return res

    @classmethod
    def write(cls, events, values):
        if len(set(events)) != cls.search([('id', 'in', map(int, events))],
                count=True):
            cls.raise_user_error('access_error', cls.__doc__)
        super(Event, cls).write(events, values)
        if len(set(events)) != cls.search([('id', 'in', map(int, events))],
                count=True):
            cls.raise_user_error('access_error', cls.__doc__)

    @classmethod
    def delete(cls, events):
        if len(set(events)) != cls.search([('id', 'in', map(int, events))],
                count=True):
            cls.raise_user_error('access_error', cls.__doc__)
        super(Event, cls).delete(events)
