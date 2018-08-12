===============================
Graphviz extension for Docutils
===============================

A Docutils extension that replaces inline Graphviz definitins with inline SVGs or PNGs!

refer: https://github.com/sprin/markdown-inline-graphviz

Install `Graphviz <https://www.graphviz.org/>`_ first! The command "dot" should be in system PATH.


register::

    import docutils_graphviz
    from docutils.parsers.rst import directives

    directives.register_directive('dot', docutils_graphviz.Graphviz)

example:

.. dot:: svg
    :widht: 100%
    :height: 100%
    :alt: image.svg

    digraph G {
        node[fontname="simsun"]
        edge[fontname="simsun"]

        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
