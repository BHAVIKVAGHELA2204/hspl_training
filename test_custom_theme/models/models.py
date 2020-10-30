# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ../../hspl_training/test_custom_theme(models.Model):
#     _name = '../../hspl_training/test_custom_theme.../../hspl_training/test_custom_theme'
#     _description = '../../hspl_training/test_custom_theme.../../hspl_training/test_custom_theme'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
