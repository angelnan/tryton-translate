#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from ..pool import Pool
from .test import *
from .model import *
from .mptt import *
from .import_data import *
from .export_data import *
from .trigger import *
from .access import *
from .wizard import *
from .workflow import *
from .copy import *


def register():
    Pool.register(
        Boolean,
        BooleanDefault,
        Integer,
        IntegerDefault,
        IntegerRequired,
        Float,
        FloatDefault,
        FloatRequired,
        FloatDigits,
        Numeric,
        NumericDefault,
        NumericRequired,
        NumericDigits,
        Char,
        CharDefault,
        CharRequired,
        CharSize,
        CharTranslate,
        Text,
        TextDefault,
        TextRequired,
        TextSize,
        TextTranslate,
        Sha,
        ShaDefault,
        ShaRequired,
        Date,
        DateDefault,
        DateRequired,
        DateTime,
        DateTimeDefault,
        DateTimeRequired,
        DateTimeFormat,
        Time,
        TimeDefault,
        TimeRequired,
        TimeFormat,
        One2One,
        One2OneTarget,
        One2OneRelation,
        One2OneRequired,
        One2OneRequiredRelation,
        One2Many,
        One2ManyTarget,
        One2ManyRequired,
        One2ManyRequiredTarget,
        One2ManyReference,
        One2ManyReferenceTarget,
        One2ManySize,
        One2ManySizeTarget,
        One2ManySizePYSON,
        One2ManySizePYSONTarget,
        Many2Many,
        Many2ManyTarget,
        Many2ManyRelation,
        Many2ManyRequired,
        Many2ManyRequiredTarget,
        Many2ManyRequiredRelation,
        Many2ManyReference,
        Many2ManyReferenceTarget,
        Many2ManyReferenceRelation,
        Many2ManySize,
        Many2ManySizeTarget,
        Many2ManySizeRelation,
        Reference,
        ReferenceTarget,
        ReferenceRequired,
        Property,
        Selection,
        SelectionRequired,
        Dict,
        DictDefault,
        DictRequired,
        Singleton,
        URLObject,
        ModelSQLRequiredField,
        MPTT,
        ImportDataBoolean,
        ImportDataInteger,
        ImportDataIntegerRequired,
        ImportDataFloat,
        ImportDataFloatRequired,
        ImportDataNumeric,
        ImportDataNumericRequired,
        ImportDataChar,
        ImportDataText,
        ImportDataSha,
        ImportDataDate,
        ImportDataDateTime,
        ImportDataSelection,
        ImportDataMany2OneTarget,
        ImportDataMany2One,
        ImportDataMany2ManyTarget,
        ImportDataMany2Many,
        ImportDataMany2ManyRelation,
        ImportDataOne2Many,
        ImportDataOne2ManyTarget,
        ImportDataReferenceSelection,
        ImportDataReference,
        ExportDataTarget,
        ExportData,
        ExportDataTarget2,
        ExportDataRelation,
        Triggered,
        TriggerAction,
        TestAccess,
        TestWizardStart,
        WorkflowedModel,
        CopyOne2Many,
        CopyOne2ManyTarget,
        CopyOne2ManyReference,
        CopyOne2ManyReferenceTarget,
        module='test', type_='model')
    Pool.register(
        TestWizard,
        module='test', type_='wizard')
