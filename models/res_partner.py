from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("approved", "Approve"),
            ("cancelled", "Cancel"),
        ],
        required=True,
        default="draft",
        string="Approval Status"
    )
    approver_id = fields.Many2one('res.users', string='Approved By')

    def action_approve(self):
        for rec in self:
            rec.state = 'approved'
            rec.approver_id = self.env.user

    def action_reset(self):   
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):   
        for rec in self:
            rec.state = 'cancelled'