#This file is part jasper_reports module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.transaction import Transaction
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['Sale', 'SaleReport']
__metaclass__ = PoolMeta


class Sale:
    'Sale'
    __name__ = 'sale.sale'

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        cursor.execute("UPDATE ir_action_report SET "\
                "report = 'sale_jreport/sale.jrxml', "\
                "extension = 'pdf' "\
                "WHERE report_name = 'sale.sale'")
        super(Sale, cls).__register__(module_name)


class SaleReport(JasperReport):
    __name__ = 'sale.sale'
