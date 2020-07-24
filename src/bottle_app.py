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
from bottle import default_app, route, static_file# , debug
from main import Main
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
PARDIR = os.path.abspath(os.path.join(BASEDIR, os.pardir))
HTMLDIR = os.path.abspath(os.path.join(PARDIR, "docs", "build", "html"))
@route('/')
def game_world():
    """Roteia o caminho / para o jogo do quarto."""
    return static_file('index.html', root=BASEDIR, mimetype='text/html')

@route('/oi')
def oi_mundo():
    """Roteia o caminho / para o jogo do quarto."""
    return 'Tutorial Dois - ensaiando uma nova rota'

@route('/vs')
def vs_mundo():
    """Roteia o caminho /vs para retornar a versão do sistema."""
    return 'Tutorial Dois - Versão do sistema: {}'.format(Main().get_versao())

@route('/<filename:re:.*[.]py>')
def py_mundo(filename):
    """Roteia o caminho /<nome>.py para retornar arquivos python.
    
    	:param filename: O nome do arquivo.
    """
    print("py_mundo", BASEDIR, filename)
    return static_file(filename, root=BASEDIR, mimetype='text/python')

@route('/doc')
def docroot_mundo():
    """Roteia o caminho /doc para a documentação."""
    print ("docroot_mundo",HTMLDIR)
    return static_file("index.html", root=HTMLDIR, mimetype='text/html')

@route('/doc/<filename:re:.*[.]html>')
def doc_mundo(filename):
    """Roteia o caminho /<nome>.html para retornar arquivos htmls.
    
    	:param filename: O nome do arquivo.
    """
    print ("doc_mundo",HTMLDIR)
    return static_file(filename, root=HTMLDIR, mimetype='text/html')

@route('/doc/<filename:re:.*[.]css>')
def css_mundo(filename):
    """Roteia o caminho /<nome>.css para retornar arquivos css.
    
    	:param filename: O nome do arquivo.
    """
    return static_file(filename, root=HTMLDIR, mimetype='text/css')

   
# debug(True)

application = default_app()


if __name__ == "__main__":
    #print(BASEDIR, os.path.abspath(BASEDIR), PARDIR, HTMLDIR)
    bottle.run(host='localhost', port=8000)
