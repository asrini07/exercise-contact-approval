from odoo import models, fields, api

class SalesQuotation(models.Model):
    _inherit = 'purchase.order'