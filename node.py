"""
@package    htmlwriter
@brief      Class representing an HTML node

@date       8/3/2024
@updated    8/3/2024

@author     Preston Buterbaugh
"""
# Imports
from __future__ import annotations

from typing import List, Dict

from htmlwriter.exceptions import NodeTypeException, DOMTreeException, AttributeTypeMismatch


SELF_CLOSING_TAGS = [
    'img',
    'br',
    'hr',
    'input'
]

BOOLEAN_ATTRIBUTES = [
    'checked',
    'disabled'
]


class Node:
    """
    @brief  Class representing an HTML node
    """
    def __init__(self, tag_name: str, attributes: Dict | None = None, content: str | List | None = None):
        """
        @brief  Constructor
        @param  tag_name   (str):         A string representing the name of the tag to be added
        @param  attributes (Dict):        A dictionary with key-value pairs representing node attributes and values
        @param  content    (str or List): The contents of the tag, either as a string of text or a list of Nodes
        """
        # Handle parameter defaults
        if attributes is None:
            attributes = {}
        if content is None and tag_name not in SELF_CLOSING_TAGS:
            content = []

        # Check type of content
        if type(content) is not str and type(content) is not list and type(content) is not None:
            raise TypeError(f'Parameter "content" expected type <str>, <list>, or <None>, but got {type(content)}')
        if type(content) is list:
            for node in content:
                if type(node) is not Node:
                    raise TypeError(f'List value for parameter "content" should only contain Node objects, but contains {type(node)}')

        # Assign field values
        self._node_id = 'Root'
        self.tag_name = tag_name
        self.attributes = attributes
        self.content = content
        self._max_id = 0

    def _update_node_ids(self, new_id: str):
        """
        @brief  Updates the node's ID and the IDs of all child nodes
        @param  new_id (str): The new ID being assigned to the root node
        """
        self._node_id = new_id
        if type(self.content) is list:
            for node in self.content:
                node._update_node_ids(new_id)

    # Get/set functions for node identification attributes
    def id(self, new_id: str | None = None) -> str | None:
        """
        @brief  Gets or sets the node's ID. Shorthand for attr('id', value)
        @param  new_id (str): The new ID to set
        @return (str or None): The node's ID after it is set
        """
        return self.attr('id', new_id)

    def classes(self, classes: str | List | None = None) -> List:
        """
        @brief  Gets all class names associated with the node, or sets all classes, overwriting any existing classes
        @param  classes (List): A list of all class names to apply to the node. For convenience, this may be specified
                                either as a space separated string, or a list of strings. If not specified, no change
                                is made to the node's classes
        @return (List) A list containing all class names associated with the node
        """
        if classes is None:
            try:
                return self.attributes['class']
            except KeyError:
                return []
        else:
            if type(classes) is str:
                classes = classes.split(' ')
            self.attributes['class'] = classes
            return classes

    def add_class(self, class_name: str):
        """
        @brief  Adds a new class to the node
        @param  class_name (str): The name of the class to add
        """
        if 'class' in self.attributes.keys():
            if class_name not in self.attributes['class']:
                self.attributes['class'].append(class_name)
        else:
            self.attributes['class'] = [class_name]

    def remove_class(self, class_name: str):
        """
        @brief  Removes a class name from the node
        @param  class_name (str): The name of the class to remove
        """
        if 'class' in self.attributes.keys() and class_name in self.attributes['class']:
            self.attributes['class'].remove(class_name)

    # Get/set functions for link attributes
    def href(self, href: str | None = None) -> str | None:
        """
        @brief  Gets or sets the href attribute for the node. Shorthand for attr('href', value)
        @param  href (str): A new href to set for the node
        @return (str or None): The current value of the href attribute after the function.
        """
        return self.attr('href', href)

    def target(self, target: str | None = None) -> str | None:
        """
        @brief  Gets or sets the target attribute for the node. Shorthand for attr('target', value)
        @param  target (str): A new target to set for the node
        @return (str or None): The current value of the target attribute after the function.
        """
        return self.attr('target', target)

    # Get/set functions for external resource tag attributes (img, iframe)
    def src(self, src: str | None = None) -> str | None:
        """
        @brief  Gets or sets the source attribute for the node. Shorthand for attr('src', value)
        @param  src (str): A new source to set for the node
        @return (str or None): The current value of the source attribute after the function.
        """
        return self.attr('src', src)

    def width(self, width: str | None = None) -> str | None:
        """
        @brief  Gets or sets the width attribute for the node. Shorthand for attr('width', value)
        @param  width (str): A new width value for the node
        @return (str or None): The current value of the width attribute after the function
        """
        return self.attr('width', width)

    def height(self, height: str | None = None) -> str | None:
        """
        @brief  Gets or sets the height attribute for the node. Shorthand for attr('height', value)
        @param  height (str): A new height value for the node
        @return (str or None): The current value of the height attribute after the function
        """
        return self.attr('height', height)

    # Get/set functions for form element attributes
    def for_attr(self, for_value: str | None = None) -> str | None:
        """
        @brief  Gets or sets the "for" attribute for the node. Shorthand for attr('for', value)
        @param  for_value (str): A new "for" value for the node
        @return (str or None): The current value of the "for" attribute after the function
        """
        return self.attr('for', for_value)

    def name(self, name: str | None = None) -> str | None:
        """
        @brief  Gets or sets the name attribute for the node. Shorthand for attr('name', value)
        @param  name (str): A new name value for the node
        @return (str or None): The current value of the name attribute after the function
        """
        return self.attr('name', name)

    def type_attr(self, type_value: str | None = None) -> str | None:
        """
        @brief  Gets or sets the type attribute for the node. Shorthand for attr('type', value)
        @param  type_value (str): A new type value for the node
        @return (str or None): The current value of the type attribute after the function
        """
        return self.attr('type', type_value)

    def placeholder(self, placeholder: str | None = None) -> str | None:
        """
        @brief  Gets or sets the placeholder attribute for the node. Shorthand for attr('placeholder', value)
        @param  placeholder (str): A new placeholder value for the node
        @return (str or None): The current value of the placeholder attribute after the function
        """
        return self.attr('placeholder', placeholder)

    def checked(self, checked: bool | None = None) -> bool | None:
        """
        @brief  Gets or sets the checked attribute for the node. Shorthand for attr('checked', value)
        @param  checked (str): A boolean value for the "checked" attribute of the node
        @return (str or None): The current value of the "checked" attribute after the function
        """
        return self.attr('checked', checked)

    def disabled(self, disabled: bool | None = None) -> bool | None:
        """
        @brief  Gets or sets the disabled attribute for the node. Shorthand for attr('disabled', value)
        @param  disabled (str): A boolean value for the "disabled" attribute of the node
        @return (str or None): The current value of the "disabled" attribute after the function
        """
        return self.attr('disabled', disabled)

    # Get/set functions for SVG element attributes
    def transform(self, transform: str | None = None) -> str | None:
        """
        @brief  Gets or sets the transform attribute for a node. Shorthand for attr('transform', value)
        @param  transform (str): A new transform value for the node
        @return (str or None): The current value of the transform attribute after the function
        """
        return self.attr('transform', transform)

    def fill(self, fill: str | None = None) -> str | None:
        """
        @brief  Gets or sets the fill attribute for a node. Shorthand for attr('fill', value)
        @param  fill (str): A new fill value for the node
        @return (str or None): The current value of the fill attribute after the function
        """
        return self.attr('fill', fill)

    def stroke(self, stroke: str | None = None) -> str | None:
        """
        @brief  Gets or sets the stroke attribute for a node. Shorthand for attr('stroke', value)
        @param  stroke (str): A new stroke value for the node
        @return (str or None): The current value of the stroke attribute after the function
        """
        return self.attr('stroke', stroke)

    def d(self, d: str | None = None) -> str | None:
        """
        @brief  Gets or sets the d attribute for a node. Shorthand for attr('d', value)
        @param  d (str): A new d value for the node
        @return (str or None): The current value of the d attribute after the function
        """
        return self.attr('d', d)

    # Get/set function for the style attribute
    def style(self, style: str | None) -> str | None:
        """
        @brief  Gets or sets the CSS style attribute for the node. Shorthand for attr('style', value)
        @param  style (str): A new CSS style for the node
        @return (str or None): The current value of the CSS style attribute after the function
        """
        return self.attr('style', style)

    # General attribute get/set function
    def attr(self, attribute: str, value: str | bool | None = None) -> str | bool | None:
        """
        @brief  Sets an attribute on the node, or returns the existing value
        @param  attribute (str): The name of the attribute to get or set
        @param  value     (str or bool): A new value to set for the attribute. Affects the function's behavior as follows
                                         - If unspecified, returns the existing attribute value, or None if this attribute is not set
                                         - If specified as an empty string, removes this attribute from the node
                                         - Otherwise, sets the attribute to the specified string
        @return (str, bool, or None): The current value of the attribute after the function, or None if the attribute is
                                      not set on the node
        """
        if value is None:
            try:
                if attribute == 'class':
                    return ' '.join(self.attributes[attribute])
                return self.attributes[attribute]
            except KeyError:
                if attribute in BOOLEAN_ATTRIBUTES:
                    return False
                else:
                    return None
        elif value == '':
            self.attributes.pop(attribute, None)
            return None
        else:
            # Type check supplied value
            if attribute in BOOLEAN_ATTRIBUTES:
                expected_type = bool
            else:
                expected_type = str
            if type(value) is not expected_type:
                raise AttributeTypeMismatch(f"Attribute '{attribute}' expects type '{expected_type}'. Got '{type(value)}'")

            # Set attribute
            if attribute == 'class':
                value = value.split(' ')
            self.attributes[attribute] = value
            return value

    # Functions for accessing node content
    def text_content(self, text: str | None = None) -> str | None:
        """
        @brief  Gets or sets a node's text content
        @param  text (str): The text to set as the content of the node. If unspecified, returns the current text content
        @return (str or None): The text content of the node after it is set. None is returned if the node contains HTML
                               nodes instead of text
        """
        if text is None:
            if type(self.content) is str:
                return self.content
            elif type(self.content) is list and len(self.content) == 0:
                return ''
            else:
                return None
        else:
            self.content = text

    def get_child_nodes(self) -> List | None:
        """
        @brief  Returns a list of all the node's child nodes
        @return A list of all child nodes, or none if it is a text node or a self-closing tag
        """
        if self.content is None or (type(self.content) is str and self.content != ''):
            return None
        elif self.content == '':
            return []
        else:
            return self.content

    def get_by_id(self, search_id: str) -> Node | None:
        """
        @brief  Gets a child element of the node that matches the specified ID
        @param  search_id (str): The ID to search for
        @return (Node or None) The node with the matching ID, or None if no node found
        """
        if type(self.content) is not list:
            return None
        else:
            for node in self.content:
                if 'id' in node.attributes.keys() and node.attributes['id'] == search_id:
                    return node
                if type(node.content) is list:
                    sub_node = node.get_by_id(search_id)
                    if sub_node is not None:
                        return sub_node
            return None

    def get_by_class_name(self, class_name: str) -> List:
        """
        @brief  Gets a list of all child elements of the node that contain the specified class
        @param  class_name (str): The class name to search for
        @return (List) A list of all nodes containing the specified class
        """
        matching_nodes = []
        if type(self.content) is list:
            for node in self.content:
                if 'class' in node.attributes.keys() and class_name in node.attributes['class']:
                    matching_nodes.append(node)
                if type(node.content) is list:
                    matching_nodes = matching_nodes + node.get_by_class_name(class_name)
        return matching_nodes

    def get_by_tag_name(self, tag_name: str) -> List:
        """
        @brief  Gets a list of all child elements of the node that have the specified tag name
        @param  tag_name (str): The tag name to search for
        @return (List) A list of all nodes matching the specified tag name
        """
        matching_nodes = []
        if type(self.content) is list:
            for node in self.content:
                if node.tag_name == tag_name:
                    matching_nodes.append(node)
                if type(node.content) is list:
                    matching_nodes = matching_nodes + node.get_by_tag_name(tag_name)
        return matching_nodes

    # Functions for mutating node content
    def insert_before(self, before_node: Node, insert_node: Node):
        """
        @brief  Inserts a new node into the node's DOM tree, before the specified node
        @param  before_node (Node): The node before which to insert the new node
        @param  insert_node (Node): The node to be inserted
        """
        # Check node type
        if type(self.content) is str and self.content != '':
            raise NodeTypeException('Cannot insert an HTML node into a node with text content')
        elif self.content is None:
            raise NodeTypeException('Cannot insert an HTML node into a self-closing tag')
        else:
            # Find node to insert before
            before_index = -1
            for i, node in enumerate(self.content):
                if node._node_id == before_node._node_id:
                    before_index = i
                    break

            # Raise exception if node not found
            if before_index == -1:
                raise DOMTreeException('Node insertion failed. Node to insert before is not a child of the node on which the insertion is to be made')

            # Insert node
            self._max_id = self._max_id + 1
            insert_node._update_node_ids(f'{self._node_id}>{self._max_id}')
            self.content = self.content[0:before_index] + [insert_node] + self.content[before_index:]

    def append_child(self, append_node: Node):
        """
        @brief  Inserts a new node at the end of the node's DOM tree
        @param  (Node) append_node: The node to append
        """
        # Check node type
        if type(self.content) is str and self.content != '':
            raise NodeTypeException('Cannot insert HTML node into text node')
        elif self.content is None:
            raise NodeTypeException('Cannot insert HTML node into self-closing tag')
        else:
            if type(self.content) is str:
                self.content = []
            self._max_id = self._max_id + 1
            append_node._update_node_ids(f'{self._node_id}>{self._max_id}')
            self.content.append(append_node)

    def remove_child(self, remove_node: Node):
        """
        @brief  Removes a node from the node's DOM tree
        @param  remove_node (str): The node to remove
        """
        # Check node type
        if type(self.content) is str:
            raise NodeTypeException('Cannot remove HTML element from text node')
        elif self.content is None:
            raise NodeTypeException('Cannot remove HTML element from self-closing tag')
        else:
            # Find node to remove
            remove_index = -1
            for i, node in enumerate(self.content):
                if node._node_id == remove_node._node_id:
                    remove_index = i
                    break

            # Raise exception if node not found
            if remove_index == -1:
                raise DOMTreeException('Node removal failed. The node to be removed is not a child of the node to remove it from')

            self.content.pop(remove_index)
