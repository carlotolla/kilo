# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Um - respondendo dúvidas do SuperPython.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

- Como associar um evento a uma imagem
- Como combinar cenas em salas diferentes
- Como capturar o teclado

Sem Classes neste modulo:

Changelog
---------
.. versionadded::    20.07
        Adiciona o gerenciador de chamadas http via bottle.

"""
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Tutorial Dois - aprendendo Git e Bottle'

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - ensaiando uma nova rota'

application = default_app()

