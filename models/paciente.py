# -*- coding: utf-8 -*-

from odoo import models, fields

class paciente(models.Model):
    _name = 'gestion_hospital.paciente'
    _description = 'Paciente del hospital'

    nombre_apellido = fields.Char(
        string='Nombre y apellidos del paciente',
    )

    sintomas = fields.Char(
        string='Sintomas del paciente'
    )
    
    diagnostico_ids = fields.One2many(
        string='diagnostico_ids',
        comodel_name='gestion_hospital.diagnostico',
        inverse_name='paciente_id',
    )
    
    
