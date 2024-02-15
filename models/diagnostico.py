from odoo import models, fields

class diagnostico(models.Model):
    _name = 'gestion_hospital.diagnostico'
    _description = 'Diagnostico dado a un paciente por un medico'
    
    paciente_id = fields.Many2one(
        string='Paciente',
        comodel_name='gestion_hospital.paciente',
        ondelete='cascade',
    )

    medico_id = fields.Many2one(
        string='Medico',
        comodel_name='gestion_hospital.medico',
        ondelete='cascade',
    )
    
    descripcion = fields.Char(
        string='Descripcion del diagnostico'
    )