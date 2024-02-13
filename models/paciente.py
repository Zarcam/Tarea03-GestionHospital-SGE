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

    diagnostico = fields.One2many('gestion_hospital.diagnostico', 'paciente')
    
