from odoo import fields,models,api

class StudentInherit(models.Model):
    _inherit = "logic.students"
    gender = fields.Selection(selection=[('male','Male'),('female','Female'),('other','Other')],string="Gender")
