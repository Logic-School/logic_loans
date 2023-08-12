from odoo import models, api, fields

class FeeStructureLine(models.Model):
    _name = "loan.fee.structure.line"
    # sl_no = fields.Integer(string="SL No")
    company_id = fields.Many2one(
            'res.company', store=True, copy=False,
            string="Company",
            default=lambda self: self.env.user.company_id.id,
            readonly=True)
    currency_id = fields.Many2one(
            'res.currency', string="Currency",
            related='company_id.currency_id',
            default=lambda
            self: self.env.user.company_id.currency_id.id,
            readonly=True)
    particular = fields.Text(string="Particular")
    amount = fields.Monetary(string="Amount")
    loan_letter_id = fields.Many2one('loan.letter')
