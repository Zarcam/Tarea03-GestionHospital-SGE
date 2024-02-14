from odoo import models, fields

class diagnostico(models.Model):
    _name = 'gestion_hospital.diagnostico'
    _description = 'Diagnostico dado a un paciente por un medico'

    paciente = fields.Many2one('gestion_hospital.paciente')
    medico = fields.Many2one('gestion_hospital.medico')

    
    paciente_id = fields.Many2one(
        string='paciente_id',
        comodel_name='gestion_hospital.paciente',
        ondelete='cascade',
    )
  
    medico_id = fields.Many2one(
        string='medico_id',
        comodel_name='gestion_hospital.medico',
        ondelete='cascade',
    )
    
    

    descripcion = fields.Char(
        string='Descripcion del diagnostico'
    )