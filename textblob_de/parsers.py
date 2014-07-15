# -*- coding: utf-8 -*-
'''Code imported from textblob main package.

:repo: `https://github.com/sloria/TextBlob`_
:source: textblob/en/parsers.py
:version: 2013-10-21 (a88e86a76a)

:modified: July 2014 <m.killer@langui.ch>

'''
from __future__ import absolute_import
from textblob.base import BaseParser
from textblob_de.de import parse as pattern_parse


class PatternParser(BaseParser):

    '''Parser that uses the implementation in Tom de Smedt's pattern library.
    http://www.clips.ua.ac.be/pages/pattern-de#parser
    '''

    def parse(self, text):
        '''Parses the text.'''
        return pattern_parse(text)
