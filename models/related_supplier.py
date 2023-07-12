from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class related_supplier(models.Model):
    _name = 'related.supplier'

    name = fields.Char()
    gender = fields.Selection([('male', 'Male'),('female', 'Female')])
