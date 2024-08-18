"""
@package    htmlwriter
@brief      A class representing an HTML document

@date       8/2/2024
@updated    8/17/2024

@author     Preston Buterbaugh
"""
# Imports
from enum import Enum
from typing import List, Dict

from htmlwriter.node import Node
from htmlwriter.exceptions import HTMLWriterException, DOMTreeException


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
        self._max_id = 0

    def add_metadata(self, metadata: Dict):
        """
        @brief  Adds a new meta tag to the document
        @param  metadata (Dict): Key-value pairs corresponding to attributes and values of the meta tag
        """
        self.metadata.append(metadata)

    def remove_metadata(self, attribute: str, value: str):
        """
        @brief  Removes a metadata attribute from the document
        @param  attribute (str): The name of a metadata attribute to remove
        @param  value     (str): The corresponding value of the metadata attribute to remove
        """
        removed = False
        for meta_tag in self.metadata:
            for key in meta_tag.keys():
                if key == attribute and meta_tag[key] == value:
                    meta_tag.pop(key, None)
                    removed = True
                    if len(meta_tag) == 0:
                        self.metadata.remove(meta_tag)
                    break
            if removed:
                break

    def add_css_file(self, filename: str):
        """
        @brief  Adds a new CSS file to the document's list
        @param  filename (str): The name of the CSS file being added
        """
        if filename not in self.css:
            self.css.append(filename)

    def remove_css_file(self, filename: str):
        """
        @brief  Removes a CSS file from the document's list
        @param  filename (str): The name of the file to remove
        """
        if filename in self.css:
            self.css.remove(filename)
        else:
            raise HTMLWriterException(f'Cannot remove CSS file "{filename}", as it is not one of the document\'s CSS files')

    def add_script_file(self, filename: str):
        """
        @brief  Adds a new JavaScript file to the document's list
        @param  filename (str): The name of the JavaScript file being added
        """
        if filename not in self.external_js:
            self.external_js.append(filename)

    def remove_script_file(self, filename: str):
        """
        @brief  Removes a JavaScript file from the document's list
        @param  filename (str): The name of the file to remove
        """
        if filename in self.external_js:
            self.external_js.remove(filename)
        else:
            raise HTMLWriterException(f'Cannot remove script file "{filename}", as it is not one of the document\'s script files')

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
            if node._node_id == before_node._node_id:
                before_index = i
                break

        # Raise exception if node was not found
        if before_index == -1:
            raise DOMTreeException('Failed to insert node. The node to insert before is not a child of document.body')

        # Insert node
        self._max_id = self._max_id + 1
        new_node._update_node_ids(str(self._max_id))
        self.dom_tree = self.dom_tree[0:before_index] + [new_node] + self.dom_tree[before_index:]

    def append_child(self, new_node: Node):
        """
        @brief  Mimics the JavaScript "document.appendChild()" method, by inserting a new HTML node to the end of the DOM tree
        @param  new_node (Node): The node to be inserted
        """
        self._max_id = self._max_id + 1
        new_node._update_node_ids(str(self._max_id))
        self.dom_tree.append(new_node)

    def remove_child(self, remove_node: Node):
        """
        @brief  Mimics the JavaScript "document.removeChild()" method, by removing an HTML node from the DOM tree
        @param  remove_node (str): The node to remove
        """
        # Find node to remove
        remove_index = -1
        for i, node in enumerate(self.dom_tree):
            if node._node_id == remove_node._node_id:
                remove_index = i
                break

        # Raise exception if node not found
        if remove_index == -1:
            raise DOMTreeException('Node removal failed. The node to be removed is not a child of document.body')

        self.dom_tree.pop(remove_index)

    def export(self, filepath: str = 'index.html', indent: str = '    ', line_limit: int = 185):
        """
        @brief  Exports the document in its current state to an HTML file
        @param  filepath   (str): The filepath to which to save the document. Defaults to "index.html" in the current directory
        @param  indent     (str): A string to use for each indentation in the document. Defaults to four spaces
        @param  line_limit (int): The number of characters after which to wrap a line if possible. Defaults to 185 characters
        """
        curr_indent = ''
        try:
            with open(filepath, 'w') as file:
                # Set doctype
                if self.doctype == Doctype.HTML5:
                    file.write(f'<!DOCTYPE html>')
                elif self.doctype == Doctype.HTML4:
                    file.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">')
                else:
                    file.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">')

                # Open html and head tags
                file.write(f'\n{curr_indent}<html>')
                curr_indent = f'{curr_indent}{indent}'
                file.write(f'\n{curr_indent}<head>')
                curr_indent = f'{curr_indent}{indent}'

                # Write meta tags
                for meta_tag in self.metadata:
                    file.write(f'\n{curr_indent}<meta')
                    for attribute in meta_tag.keys():
                        file.write(f' {attribute}="{meta_tag[attribute]}"')
                    file.write(' />')

                # Write title tag
                file.write(f'\n{curr_indent}<title>{self.title}</title>')

                # Write internal CSS
                if self.internal_css:
                    file.write(f'\n{curr_indent}<style>')
                    curr_indent = f'{curr_indent}{indent}'
                    css_lines = self.internal_css.split('\n')
                    for line in css_lines:
                        file.write(f'\n{curr_indent}{line}')
                    curr_indent = curr_indent[0:len(curr_indent) - len(indent)]
                    file.write(f'\n{curr_indent}</style>')

                # Create link tags for external CSS
                for css_file in self.css:
                    file.write(f'\n{curr_indent}<link rel="stylesheet" href="{css_file}" />')

                # Close head tag and open body tag
                curr_indent = curr_indent[0:len(curr_indent) - len(indent)]
                file.write(f'\n{curr_indent}</head>')
                if len(self.dom_tree) == 0:
                    file.write(f'\n{curr_indent}<body />')
                else:
                    file.write(f'\n{curr_indent}<body>')

                # Write body
                curr_indent = f'{curr_indent}{indent}'
                for node in self.dom_tree:
                    file.write(tag_content(node, curr_indent, indent, line_limit))

                # Write JavaScript
                if self.js:
                    file.write(f'\n{curr_indent}<script>')
                    curr_indent = f'{curr_indent}{indent}'
                    js_lines = self.js.split('\n')
                    for line in js_lines:
                        file.write(f'\n{curr_indent}{line}')
                    curr_indent = curr_indent[0:len(curr_indent) - len(indent)]
                    file.write(f'\n{curr_indent}</script>')

                # External JS
                for script_file in self.external_js:
                    file.write(f'\n{curr_indent}<script src="{script_file}"></script>')

                # Close body tag
                curr_indent = curr_indent[0:len(curr_indent) - len(indent)]
                if self.dom_tree:
                    file.write(f'\n{curr_indent}</body>')

                # Close html tag
                curr_indent = curr_indent[0:len(curr_indent) - len(indent)]
                file.write(f'\n{curr_indent}</html>')
        except FileExistsError:
            print(f'Failed to create file {filepath}. A file with that name already exists')
        except PermissionError:
            print(f'Failed to create file {filepath}. You may not have permission to create files in this location')


def tag_content(tag: Node, indent: str, indent_increment: str, line_limit: int, inline: bool = False) -> str:
    """
    @brief  Compiles a Node object into HTML text, given export file information
    @param  tag              (Node): The tag to parse
    @param  indent           (str):  The current indentation level of the document
    @param  indent_increment (str):  The text to add on to the indent when increasing indent level
    @param  line_limit       (int):  The maximum number of characters to put on a single line before wrapping if possible
    @param  inline           (bool): If no newline should be included before the tag's contents
    @return (str) The HTML text of the tag
    """
    # Write opening tag
    if inline:
        text = ''
    else:
        text = f'\n{indent}'
    text = f'{text}<{tag.tag_name}'
    for attribute in tag.attributes.keys():
        if attribute == 'class' and type(tag.attributes[attribute]) is list:
            value = ' '.join(tag.attributes[attribute])
        else:
            value = tag.attributes[attribute]
        text = f'{text} {attribute}="{value}"'
    if tag.content is None:
        text = f'{text} /'
    text = f'{text}>'

    # Check the tag type (text or tree)
    if type(tag.content) is str:
        # Check if it fits on a single line
        if len(f'{text}{tag.content}</{tag.tag_name}>') <= line_limit:
            text = f'{text}{tag.content}</{tag.tag_name}>'
        else:
            indent = f'{indent}{indent_increment}'
            remaining_content = tag.content
            while len(f'{indent}{remaining_content}') > line_limit:
                single_line = remaining_content[0:line_limit]
                remaining_content = remaining_content[line_limit:]
                text = f'{text}\n{indent}{single_line}'
            text = f'{text}\n{indent}{remaining_content}'
            indent = indent[0:len(indent) - len(indent_increment)]
            text = f'{text}\n{indent}</{tag.tag_name}>'
    elif tag.content is not None:
        # Anchor tags containing only one tag are printed on the same line
        if tag.tag_name == 'a' and len(tag.content) == 1:
            text = f'{text}<a'
            for attribute in tag.attributes.keys():
                if attribute == 'class':
                    value = ' '.join(tag.attributes[attribute])
                else:
                    value = tag.attributes[attribute]
                text = f'{text} {attribute}="{value}"'
            text = f'{text}>{tag_content(tag.content[0], indent, indent_increment, line_limit, inline=True)}'
            text = f'{text}</a>'
        else:
            indent = f'{indent}{indent_increment}'
            for child_tag in tag.content:
                text = f'{text}{tag_content(child_tag, indent, indent_increment, line_limit)}'
            indent = indent[0:len(indent) - len(indent_increment)]
            text = f'{text}\n{indent}</{tag.tag_name}>'

    return text
