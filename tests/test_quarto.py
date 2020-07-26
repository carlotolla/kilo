# -*- coding: utf-8 -*-
# kilo.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Testando quadros.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>


Classes neste modulo:

    :py:class:`TestQuarto` Testa o Jogo do Quarto.

Changelog
---------
.. versionadded::    20.07
        Documentação do tutorial.

"""
from unittest import TestCase
from unittest import mock


class TestQuarto(TestCase):
    @mock.patch(vitollino.Inventario)
    def setUp(self, inv):
        import vitollino
    
    def test_jogo(self):
        pass