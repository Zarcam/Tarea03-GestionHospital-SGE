from odoo import models, fields

class medico(models.Model):
    _name = 'gestion_hospital.medico'
    _description = 'Medico del hospital'

    nombre_apellidos = fields.Char(
        string='Nombre y apellidos del paciente',
    )

    num_colegiado = fields.Integer(
        string='Numero de colegiado'
    )

    diagnostico = fields.One2many('gestion_hospital', 'medico')