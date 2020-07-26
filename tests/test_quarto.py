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
    @mock.patch("vitollino.main.Inventario")
    @mock.patch("vitollino.main.Cena")
    @mock.patch("vitollino.main.Elemento")
    def setUp(self, inv, cen, elm):
        # import vitollino
        from quarto import JogoDoQuarto
        # self.jq = JogoDoQuarto()
    
    def test_jogo(self):
        pass