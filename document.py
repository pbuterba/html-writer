"""
@package    htmlwriter
@brief      A class representing an HTML document

@date       8/2/2024
@updated    8/3/2024

@author     Preston Buterbaugh
"""
# Imports
from enum import Enum
from typing import List, Dict

from htmlwriter.node import Node
from htmlwriter.exceptions import DOMTreeException


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
        self.max_id = 0

    def get_by_id(self, search_id: str) -> Node | None:
        """
        @brief  Mimics the JavaScript "document.getElementById()" method by fetching a DOM node matching the specified ID
        @param  search_id (str): The ID of the node to retrieve
        @return (Node or None) The matching DOM node, or None if no node with that ID is found
        """
        for node in self.dom_tree:
            if 'id' in node.attributes.keys() and node.attributes['id'] == search_id:
                return node
            if type(node.content) is list:
                sub_node = node.get_by_id(search_id)
                if sub_node is not None:
                    return sub_node
        return None

    def get_by_class_name(self, class_name: str) -> List:
        """
        @brief  Mimics the JavaScript "document.getElementsByClassName()" method by fetching a list of DOM nodes matching
                the specified class name
        @param  class_name (str): The class name to search for
        @return (List) A list containing all nodes matching the specified class name
        """
        matching_nodes = []
        for node in self.dom_tree:
            if 'class' in node.attributes().keys() and class_name in node.attributes['class']:
                matching_nodes.append(node)
            if type(node.content) is list:
                matching_nodes = matching_nodes + node.get_by_class_name(class_name)
        return matching_nodes

    def get_by_tag_name(self, tag_name: str) -> List:
        """
        @brief  Mimics the JavaScript "document.getElementsByTagName()" method by fetching a list of DOM nodes of the
                specified tag type
        @param  tag_name (str): The name of the HTML tag to search for
        @return (List) A list of all nodes of the specified tag type
        """
        matching_nodes = []
        for node in self.dom_tree:
            if node.tag_name == tag_name:
                matching_nodes.append(node)
            if type(node.content) is list:
                matching_nodes = matching_nodes + node.get_by_tag_name(tag_name)
        return matching_nodes

    def insert_before(self, before_node: Node, new_node: Node):
        """
        @brief  Mimics the JavaScript "document.insertBefore()" method, by inserting a new HTML node to the DOM tree
                immediately preceding a specified exiting node
        @param  before_node (Node): The node before which the new node should be inserted
        @param  new_node    (Node): The node to be inserted
        """
        # Find the node to insert before
        before_index = -1
        for i, node in enumerate(self.dom_tree):
            if node.id == before_node.id:
                before_index = i
                break

        # Raise exception if node was not found
        if before_index == -1:
            raise DOMTreeException('Failed to insert node. The node to insert before is not a child of document.body')

        # Insert node
        self.max_id = self.max_id + 1
        new_node.id = str(self.max_id)
        self.dom_tree = self.dom_tree[0:before_index] + [new_node] + self.dom_tree[before_index:]

    def append_child(self, new_node: Node):
        """
        @brief  Mimics the JavaScript "document.appendChild()" method, by inserting a new HTML node to the end of the DOM tree
        @param  new_node (Node): The node to be inserted
        """
        self.max_id = self.max_id + 1
        new_node.id = str(self.max_id)
        self.dom_tree.append(new_node)

    def export(self, filepath: str = 'index.html', indent: str = '    ', line_limit: int = 185):
        """
        @brief  Exports the document in its current state to an HTML file
        @param  filepath   (str): The filepath to which to save the document. Defaults to "index.html" in the current directory
        @param  indent     (str): A string to use for each indentation in the document. Defaults to four spaces
        @param  line_limit (int): The number of characters after which to wrap a line if possible. Defaults to 185 characters
        """
        pass
