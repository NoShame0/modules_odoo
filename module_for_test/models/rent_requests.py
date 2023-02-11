from odoo import fields, models, api


class IrActionsServer(models.Model):
    _inherit = 'ir.actions.server'

    custom_name = fields.Char(string="Custom Name")
    custom_description = fields.Text(string='Custom Description')
    custom_email_tl = fields.Text(string='Custom Email TL')
    custom_name_tl = fields.Text(string='Custom name TL')


class RentRequests(models.Model):
    _name = 'rent.requests'
    _description = 'Rent Requests'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    phone = fields.Char(string='Phone')

    email_tl = fields.Char(string='Email_Tl')
    person_name_tl = fields.Char(string='Team Leader')

    @api.model
    def create_request(self, vals):

        request = self.env['rent.requests'].create(vals)
        template = self.env.ref('module_for_test.email_template_rent_requests')

        if request.email_tl:
            template.send_mail(request.id, force_send=True)

