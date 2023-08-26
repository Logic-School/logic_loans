from odoo import models, fields, api

class CompanyInherit(models.Model):
    _inherit = "res.company"
    company_seal = fields.Binary(string="Company Seal")

class BaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"
    company_seal = fields.Binary(related = "company_id.company_seal")