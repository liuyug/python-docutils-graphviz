# -*- coding: utf-8 -*-
# based on https://github.com/sprin/markdown-inline-graphviz

"""
Graphviz extensions for docutils
Renders the output inline, eliminating the need to configure an output
directory.

Supports outputs types of SVG and PNG. The output will be taken from the
filename specified in the tag. Example:

.. dot:: attack_plan.svg

    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }

Requires the graphviz library (http://www.graphviz.org/)

register:

from docutils.parsers.rst import directives
directives.register_directive('dot', Graphviz)
"""
from bs4 import BeautifulSoup

from docutils import nodes
from docutils.parsers import rst

import base64
import graphviz


class Graphviz(rst.Directive):
    required_arguments = 1
    optional_arguments = 0
    has_content = True
    final_argument_whitespace = True
    option_spec = {
        'alt': rst.directives.unchanged,
        'height': rst.directives.length_or_percentage_or_unitless,
        'width': rst.directives.length_or_percentage_or_unitless,
    }

    def run(self):
        self.assert_has_content()
        content = '\n'.join(self.content)
        filetype = self.arguments[0]
        alt = self.options.get('alt', 'graphviz-image')

        try:
            src = graphviz.Source(content)
            output = src.pipe(format=filetype)

            if filetype == 'svg':
                soup = BeautifulSoup(output.decode('utf-8'), 'html5lib')
                svg = soup.find('svg')
                if svg:
                    if 'width' in self.options:
                        svg.attrs['width'] = self.options['width']
                    if 'height' in self.options:
                        svg.attrs['height'] = self.options['height']
                    img = '<div>%s</div>' % svg
                else:
                    img = output.decode('utf-8')

            if filetype == 'png':
                data_url_filetype = 'png'
                output = base64.b64encode(output).decode()
                data_path = "data:image/%s;base64,%s" % (data_url_filetype, output)
                attrs = []
                attrs.append('src="%s"' % data_path)
                attrs.append('alt="%s"' % alt)
                if 'width' in self.options:
                    attrs.append('width="%s"' % self.options['width'])
                if 'height' in self.options:
                    attrs.append('height="%s"' % self.options['height'])
                img = '<img %s />' % ' '.join(attrs)

        except Exception as err:
            raise self.error(str(err))
        return [nodes.raw('', img, format='html')]
