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

    diagnostico_ids = fields.One2many(
        string='diagnostico_ids',
        comodel_name='gestion_hospital.diagnostico',
        inverse_name='medico_id',
    )