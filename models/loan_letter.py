from odoo import fields, api, models
from datetime import datetime

class LoanLetter(models.Model):
    _name = "loan.letter"
    _display_name = 'display_name'

    date = fields.Date(string="Date",default=datetime.today())
    location = fields.Char(string="Location")
    student_id = fields.Many2one('logic.students',string="Student")
    academic_head_id = fields.Many2one('res.users',string="Academic Head",domain=lambda self: ['|',('id', 'in', self.env.ref('logic_base.academic_head_batch').users.ids),('id','in',self.env.ref('faculty.group_faculty_administrator').users.ids)])
    academic_head_name = fields.Char(string="Head Name")

    def _compute_display_name(self):
        for i in self:
            if i.student_id:
                i.display_name = i.student_id.name + ' - ' + 'LOAN LETTER'
            else:
                i.display_name = 'LOAN LETTER'

    @api.onchange('academic_head_id')
    def _on_change_academic_head(self):
        if self.academic_head_id:
            self.academic_head_name = self.academic_head_id.name

    @api.onchange('student_id')
    def _on_student_id_change(self):
        if self.student_id:
            self.student_name = self.student_id.name
            self.father_name = self.student_id.father_name
            self.course_name = self.student_id.batch_id.product_id.name
            self.title = 'ms' if self.student_id.gender=='female' else 'mr'
            self.address = self.formatted_address()
    student_name = fields.Char(string="Student Name")
    title = fields.Selection(selection=[('mr', 'Mr'), ('ms', 'Ms'), ('mrs', 'Mrs')], default='mr', string="Title")
    father_name = fields.Char(string="Father's Name")
    address = fields.Text(string="Address")
    course_name = fields.Char(string="Course Name")
    course_body = fields.Char(string="Course Body")
    course_abbrv = fields.Char(string="Course Abbreviation")
    fee_structure_lines = fields.One2many('loan.fee.structure.line','loan_letter_id',string="Fee Structure")
    def _compute_amount_total(self):
        for record in self:
            if record.fee_structure_lines:
                amounts = [fee_line.amount for fee_line in record.fee_structure_lines]
                record.amount = sum(amounts)
            else:
                record.amount = 0
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
    amount = fields.Monetary(string="Total Amount", compute="_compute_amount_total")

    def formatted_address(self):
        street1 = self.student_id.street if self.student_id.street else ""
        street2 = self.student_id.street2 if self.student_id.street2 else ""
        zip = self.student_id.zip if self.student_id.zip else ""
        city = self.student_id.city if self.student_id.city else ""
        state = self.student_id.state.name if self.student_id.state.name else ""
        address = ", ".join([street1,street2,city, state])
        address+=", Pin: "+zip
        return address

    def action_print_section(self):
        for i in self.fee_structure_lines:
            if not i.amount:
                print(i.name, 'fkghfk')
