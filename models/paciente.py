# -*- coding: utf-8 -*-

from odoo import models, fields

class paciente(models.Model):
    _name = 'gestion_hospital.paciente'
    _description = 'Paciente del hospital'

    nombre = fields.Char(
        string='Nombre del paciente',
    )

    apellidos = fields.Char(
        string='Apellidos del paciente',
    )

    sintomas = fields.Char(
        string='Sintomas del paciente'
    )
    
