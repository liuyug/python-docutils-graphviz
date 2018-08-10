===============================
Graphviz extension for Docutils
===============================

A Docutils extension that replaces inline Graphviz definitins with inline SVGs or PNGs!

refer: https://github.com/sprin/markdown-inline-graphviz

Install `Graphviz <https://www.graphviz.org/>`_ first! The command "dot" should be in system PATH.

example:

.. dot:: attack_plan.svg

    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
