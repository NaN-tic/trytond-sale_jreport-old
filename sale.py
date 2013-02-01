#This file is part jasper_reports module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.transaction import Transaction
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['SaleReport']
__metaclass__ = PoolMeta


class SaleReport(JasperReport):
    __name__ = 'sale.sale'
