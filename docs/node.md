# Node
The Node class represents a node (or HTML tag) within an HTML document. Nodes can be one of three types: text, tree, or contentless. A text node is one that contains text content.
A tree node is a node that contains other nodes. A contentless node is a node that corresponds to a self closing tag (such as an `<img>` or a `<br>`), which by definition contains
no content.

## Self-closing tags
The following tags are considered self=closing tags, and can be exported to an HTML file without a closing tag, assuming they have no content set:
+ img
+ br
+ hr
+ input

## Constructor
```
node = Node(tag_name, attributes, content)
```
*Parameters:*
+ `tag_name` - A string representing the name of the tag type being added (e.g. "div", "h1", "p").
+ `attributes` - *Optional*. A dictionary, with each key-value pairing matching an attribute and its corresponding value that should be set on the tag.
+ `content` - *Optional*. A string of text, or list of `Node` objects to be the content of the tag. If a string, the Node is considered a text node, and the value of the string is set
as the tag's text content. If it is a list of Nodes, the Node is considered a tree node, and the nodes in the list are set as its child nodes. If another type (aside from `None`) is
specified, or a list is specified that contains elements other than Nodes, a `TypeError` is raised. If this parameter is unspecified, and the tag name is not a [self-closing tag](#self-closing-tags),
the node defaults to being a tree node with no content

## Fields
The following fields are available to access on objects of the Node class:
+ `tag_name` - A string representing the node's tag name
+ `attributes` = A dictionary with each key-value pair corresponding to an attribute of the tag, and its corresponding value
+ `content` - A string representing the node's text content (if it is a text node), or a list of the nodes contained by the node (if it is a tree node). If it is a contentless node,
this field has the `None` type.

## Methods
The following methods are available to call on all objects of the Node class:

### Attribute get/set functions

#### ID
```
id(new_id)
```
Sets the tag's ID attribute, and returns a string representing the new value. Returns `None` if no ID is specified for the given node

*Parameters:*
+ `new_id` - *Optional*. A string representing a new ID for the tag. If unspecified, no change is made to the ID attribute, and the current value is returned.

#### Class names
```
classes(classes)
```
Sets the class attribute of the tag. Returns a list of strings representing the tag's new list of class names. If no class names are set on the tag, an empty list is returned.

*Parameters:*
+ `classes` - *Optional*. Either a string of comma separated class names, or a list of strings, each representing a class name for the tag. This will overwrite any existing class
names assigned to the tag. If this parameter is unspecified, no changes are made to the tag's classes, and the current list is returned.

#### Add class
```
add_class(class_name)
```
Adds a new class name to the node's list of classes

*Parameters:*
+ `class_name` - A string representing a new class name to add.

#### Remove class
```
remove_class(class_name)
```
Removes a class name from the node's list of classes

*Parameters:*
+ `class_name` - A string representing the class name to remove. If the specified class name is not one of the classes of the node, this function has no effect.

#### Href
```
href(href)
```
Sets the tag's href attribute, and returns the new value. Returns `None` if no href attribute is specified on the given node.

*Parameters:*
+ `href` - *Optional*. A string representing the new href for the tag. If unspecified, no change is made to the href, and the existing value is returned.

#### Target
```
target(target)
```
Sets the tag's target attribute, and returns the new value. Returns `None` if no target attribute is specified on the given node.

*Parameters:*
+ `target` - *Optional*. A string representing the new target for the tag. If unspecified, no change is made to the target, and the existing value is returned.

#### Src
```
src(src)
```
Sets the tag's src attribute, and returns the new value. Returns `None` if no src attribute is specified on the given node.

*Parameters:*
+ `src` - *Optional*. A string representing the new source for the tag. If unspecified, no change is made to the source, and the existing value is returned.

#### Width
```
width(width)
```
Sets the tag's width attribute, and returns the new value. Returns `None` if no width attribute is specified on the given node.

*Parameters:*
+ `width` - *Optional*. A string representing the new width for the tag. If unspecified, no change is made to the width, and the existing value is returned.

#### Height
```
height(height)
```
Sets the tag's height attribute, and returns the new value. Returns `None` if no height attribute is specified on the given node.

*Parameters:*
+ `height` - *Optional*. A string representing the new height for the tag. If unspecified, no change is made to the height, and the existing value is returned.

#### For
```
for_attr(for_value)
```
Sets the tag's for attribute, and returns the new value. Returns `None` if no for attribute is specified on the given node

*Parameters:*
+ `for_value` - *Optional*. A string representing the new for attribute for the tag. If unspecified, no change is made to the for attribute, and the existing value is returned.

#### Name
```
name(name)
```
Sets the tag's name attribute, and returns the new value. Returns `None` if no name attribute is specified on the given node.

*Parameters:*
+ `name` - *Optional*. A string representing the new name for the tag. If unspecified, no change is made to the name, and the existing value is returned.

#### Type
```
type_attr(type_value)
```
Sets the tag's type attribute, and returns the new value. Returns `None` if no type attribute is specified on the given node

*Parameters:*
+ `type_value` - *Optional*. A string representing the new type attribute for the tag. If unspecified, no change is made to the type attribute, and the existing value is returned.

#### Placeholder
```
placeholder(placeholder)
```
Sets the tag's placeholder attribute, and returns the new value. Returns `None` if no placeholder attribute is specified on the given node.

*Parameters:*
+ `placeholder` - *Optional*. A string representing the new placeholder for the tag. If unspecified, no change is made to the placeholder, and the existing value is returned.

#### Checked
```
checked(checked)
```
Sets the tag's checked status, and returns the new value. If the checked value has never been set on the node, it defaults to `False`.

*Parameters:*
+ `checked` - *Optional*. A boolean value representing if the node's checked flag should be set or not. If unspecified, no change is made to the checked flag, and the current value
is returned.

#### Disabled
```
disabled(disabled)
```
Sets the tag's disabled status, and returns the new value. If the disabled value has never been set on the node, it defaults to `False`.

*Parameters:*
+ `disabled` - *Optional*. A boolean value representing if the node's disabled flag should be set or not. If unspecified, no change is made to the disabled flag, and the current
value is returned.

#### Transform
```
transform(transform)
```
Sets the tag's transform attribute, and returns the new value. Returns `None` if no transform attribute is specified on the given node.

*Parameters:*
+ `transform` - *Optional*. A string representing the new transform value for the tag. If unspecified, no change is made to the transform property, and the existing value is returned.

#### Fill
```
fill(fill)
```
Sets the tag's fill attribute, and returns the new value. Returns `None` if no fill attribute is specified on the given node.

*Parameters:*
+ `fill` - *Optional*. A string representing the new fill value for the tag. If unspecified, no change is made to the fill property, and the existing value is returned.

#### Stroke
```
stroke(stroke)
```
Sets the tag's stroke attribute, and returns the new value. Returns `None` if no stroke attribute is specified on the given node.

*Parameters:*
+ `stroke` - *Optional*. A string representing the new stroke value for the tag. If unspecified, no change is made to the stroke property, and the existing value is returned.

#### D
```
d(d)
```
Sets the tag's d attribute, and returns the new value. Returns `None` if no d attribute is specified on the given node.

*Parameters:*
+ `d` - *Optional*. A string representing the new d value for the tag. If unspecified, no change is made to the d path, and the existing value is returned.

#### Style
```
style(style)
```
Sets the tag's style attribute, and returns the new value. Returns `None.` if no style attribute is specified on the given node.

*Parameters:*
+ `style` - *Optional*. A string representing CSS code to set as the new style attribute for the tag. If unspecified, no change is made to the inline CSS, and the existing value is
returned.

#### Attribute
```
attr(attribute, value)
```
Sets the specified attribute on the tag to the specified value, and returns the new value. Returns `None` if that attribute is not specified on the given node. No check is performed
to ensure that the specified attribute is a valid HTML attribute, the text provided is directly copied into the HTML file. However, if a non-boolean value is specified when the attribute
is "checked" or "disabled", or if a non-string value is specified otherwise, a `AttributeTypeMismatch` exception is raised.

*Parameters:*
+ `attribute` - The name of the attribute to set on the node.
+ `value` - *Optional*. A string or boolean value representing the new value to set for the specified attribute. If unspecified, no change is made to the attribute, and the current
value is returned.

### Get/set functions for node contents

#### Text content
```
text_content(text)
```
Sets the text content of a text node, and returns a string representing the new text content. If the node is a tree node, but contains no nodes, the text content is considered to
be an empty string. If the node is a tree node and does contain nodes, or the node is a contentless node, `None` is returned, as the node does not have text content.

*Parameters:*
+ `text` - *Optional*. The new text content for the node. If specified, this automatically changes the node to a text node, and overwrites the node's existing content.
If unspecified, the text content is not updated, and the current value is returned.

#### Get child nodes
```
get_child_nodes()
```
Returns a list of the child nodes of a tree node. If the node is a text node, but contains no text, an empty list is returned. If it does contain text, or the node is a contentless
node, `None` is returned, as these are considered not to have a concept of child nodes.

#### Get by ID
```
get_by_id(search_id)
```
Mimics the functionality of JavaScript's `document.getElementById()` function, but specifically searches within the node on which the method is called. Allows the user to select
an element that appears within the node by its HTML ID attribute. This performs a linear search through the node's children, starting with the first node and working down,
recursing through any nodes contained within each node it searches. As soon as a node with the matching ID is found, it returns the `Node` object, meaning that if there is more
than one node in the searched node with the same ID, it will return the first one that appears. If no element with the matching ID is found, or the node is a text or contentless
node, `None` is returned.

*Parameters:*
+ `search_id` - A string representing the ID to search for.

#### Get by class name
```
get_by_class_name(class_name)
```
Mimics the functionality of JavaScript's `document.getElementsByClassName()` function, but specifically searches within the node on which the method is called. Allows the user to
select elements that appear in the node by their HTML class names. This searches through all of the node's child nodes, and returns all that have the specified class name as one of
its classes. Returns a list of `Node` objects. An empty list is returned if no nodes match the given class name, or the node is a text or contentless node.

*Parameters:*
+ `class_name` - A string representing the class name to search for.

#### Get by tag name
```
get_by_tag_name(tag_name)
```
Mimics the functionality of JavaScript's `document.getElementsByTagName()` function, but specifically searches within the node on which the method is called. Allows the user to
select elements that appear within the node by their HTML tag type. This searches through all of the node's child nodes, and returns all that are of the specified tag. Returns a
list of `Node` objects. An empty list is returned if no matching tags are found, or the node is a text or contentless node.

*Parameters:*
+ `tag_name` - A string representing the tag name to search for.

#### Insert before
```
insert_before(before_node, insert_node)
```
Mimics the functionality of JavaScript's `insertBefore()` function, allowing the user to insert a new child node, such that it appears immediately before a specified existing child
node. If the specified node to insert before is not a child of the node on which the method is called, a `DOMTreeException` is raised. If the function is called on a text or contentless
node, a `NodeTypeException` is raised.

*Parameters:*
+ `before_node` - A `Node` object representing a node that is already in the element, before which the new node should be inserted.
+ `insert_node` - A `Node` object that should be inserted as a child element.

#### Append child
```
append_child(new_node)
```
Mimics the functionality of JavaScript's `appendChild()` function, allowing the user to insert a new node at the end of the node on which the method is called. If called on a text or
contentless node, a `NodeTypeException` is raised.

*Parameters:*
+ `new_node` - A `Node` object representing the node to append.

#### Remove child
```
remove_child(remove_node)
```
Mimics the functionality of JavaScript's `removeChild()` function, allowing the user to remove a child node from the node on which the method is called. If called on a text or
contentless node, a `NodeTypeException` is raised. If the specified node is not a child of the node on which the method is called, a `DOMTreeException` is raised.

*Parameters:*
+ `remove_node` - A `Node` object representing the node to remove.