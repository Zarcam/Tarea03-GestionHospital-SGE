from odoo import models, fields

class diagnostico(models.Model):
    _name = 'gestion_hospital.diagnostico'
    _description = 'Diagnostico dado a un paciente por un medico'

    paciente = fields.Many2one('gestion_hospital.paciente')
    medico = fields.Many2one('gestion_hospital.medico')

    descripcion = fields.Char(
        string='Descripcion del diagnostico'
    )