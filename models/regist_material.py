from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class regist_material(models.Model):
    _name = 'regist.material'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    type = fields.Selection([('fabric', 'Fabric'),('jeans', 'Jeans'),('cotton', 'Cotton')] ,required=True)
    buy_price = fields.Float(required=True)
    related_supplier = fields.Many2one('related.supplier', required=True)
    
    @api.constrains('buy_price')
    def _validation_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError('Nilai Material Buy Price TIdak Boleh Kurang Dari 100!')
    