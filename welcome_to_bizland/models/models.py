# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ../../hspl_training/welcome_to_bizland(models.Model):
#     _name = '../../hspl_training/welcome_to_bizland.../../hspl_training/welcome_to_bizland'
#     _description = '../../hspl_training/welcome_to_bizland.../../hspl_training/welcome_to_bizland'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
