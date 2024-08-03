"""
@package    html_writer
@brief      A class representing an HTML document

@date       8/2/2024
@updated    8/2/2024

@author     Preston Buterbaugh
"""
# Imports
from enum import Enum
from typing import List, Dict


class Doctype(Enum):
    """
    @brief  Enumeration of the different types of HTML documents
    """
    HTML5 = 0
    HTML4 = 1
    XHTML = 2


class Document:
    """
    @brief  Class representing an HTML document
    """
    def __init__(self, title: str, doctype: Doctype = Doctype.HTML5, metadata: List | None = None, css: List | None = None):
        """
        @brief  Constructor
        @param  title    (str):     The title for the page
        @param  doctype  (Doctype): The doctype for the document. Defaults to HTML5
        @param  metadata (List):    A list of dictionaries corresponding to meta tags, with each key-value pair representing
                                    a meta attribute and value. Defaults to "charset=utf-8"
        @param  css      (List):    A list of strings representing URLs for CSS files to apply to the page. Defaults to
                                    an empty list
        """
        if metadata is None:
            metadata = [{'charset': 'utf-8'}]
        if css is None:
            css = []
        self.doctype = doctype
        self.metadata = metadata
        self.title = title
        self.internal_css = ''
        self.css = css
        self.dom_tree = []
        self.js = ''
        self.external_js = []
