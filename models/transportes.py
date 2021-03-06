# -*- coding: utf-8 -*-

from dataclasses import field
from datetime import datetime
import string
from odoo import models, fields, api


class barcos(models.Model):
    _name = 'transportes.barcos'
    _description = 'Barcos'

    name = fields.Char(string='Barco', required=True)
    codigo_barco = fields.Char(string='Código', required=True)


class rutas(models.Model):
    _name = 'transportes.rutas'
    _description = 'Rutas'

    name = fields.Char(string='Ruta', required=True)
    codigo_ruta = fields.Char(string='Código', required=True)

class productos(models.Model):
    _inherit = 'product.template'
    _description = 'Productos'

   
    embarque_enlace = fields.Many2one('transportes.embarque')

    costo_embarque = fields.Float(string='Costo trasnporte', required=True)

class embarque(models.Model):
    _name = 'transportes.embarque'
    _description = 'Embarque'

    name = fields.Char(string='Embarque', required=True)
    barcos = fields.Many2one('transportes.barcos', string='Barcos', required=True)
    rutas = fields.Many2one('transportes.rutas', string='Rutas', required=True)
    productos = fields.Many2many('product.template', 'embarque_enlace',
        string="Productos", required=True, ondelete='cascade')

    total_productos = fields.Float(string='Total de productos', compute='_compute_costo_trasnporte') 
    total_transporte = fields.Float(string='Total de trasnporte', compute='_compute_costo_trasnporte')     
    costo_total  = fields.Float(string='Total', compute='_compute_costo_trasnporte')

    @api.depends('productos')
    def _compute_costo_trasnporte(self):
        for rec in self:
            for record in rec.productos:
                rec.total_productos += record.list_price
                rec.total_transporte += record.costo_embarque
            rec.costo_total = rec.total_productos + rec.total_transporte 
    
