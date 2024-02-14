# -*- coding: utf-8 -*-
{
    'name': "GestionHospital",

    'summary': "Gestor de pacientes y medicos",

    'description': """
        Almacena datos de pacientes con sus diagnosticos.
        Y los datos de medicos con sus pacientes tratados.
    """,

    'author': "Alejandro Rebagliato",
    'website': "https://github.com/Zarcam/Odoo-ListaTareas-SGE",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],    
}

