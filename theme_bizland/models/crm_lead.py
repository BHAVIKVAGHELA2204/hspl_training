from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    number_of_emp = fields.Integer(string='Number of Employees')
