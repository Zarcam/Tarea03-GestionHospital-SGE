from odoo import models, fields

class medico(models.Model):
    _name = 'gestion_hospital.medico'
    _description = 'Medico del hospital'

    nombre = fields.Char(
        string='Nombre del paciente',
    )

    apellidos = fields.Char(
        string='Apellidos del paciente',
    )

    num_colegiado = fields.Integer(
        string='Numero de colegiado'
    )