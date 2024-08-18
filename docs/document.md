# Document
The document object represents an HTML document. It contains all the information contained in the `<head>` tag, as well as the contents of the `<body>` tag, which is a collection
of [`Node`](node.md) objects.

## Constructor
```
document = Document(title, doctype, metadata, css)
```
*Parameters:*
+ `title` - A string representing the document's title. This is the content of the `<title>` tag, and displays on the page's tab in a browser.
+ `doctype` - *Optional*. A `Doctype` value representing the document's language type. If unspecified, defaults to HTML 5.
+ `metatata` - *Optional*. A list of dictionaries representing document metadata. Each dictionary in the list represents a `<meta>` tag, with each key-value pair representing an
attribute and value of the meta tag.
+ `css` - *Optional*. A list of strings, each corresponding to the name of or filepath to a CSS file to be linked to the document. `<link>` tags will be added for each CSS file.

## Fields
The following fields are available to access on objects of the Document class:
+ `doctype` - A `Doctype` value representing the document's language type
+ `metadata` - A list of dictionaries representing the document metadata. Each dictionary in the list represents a `<meta>` tag, with each key-value pair representing an
attribute and value of the meta tag.
+ `title` - A string representing the document's title. This is the content of the `<title>` tag, and displays on the page's tab in a browser.
+ `internal_css` - A string containing CSS to be applied to the page. This text is set as the content of a `<style>` tag, which is included in the document if the value of this field
is not empty
+ `css` - A list of strings each corresponding to the name of or filepath to a CSS file to be linked to the document. `<link>` tags will be added for each CSS file.
+ `dom_tree` - A list of `Node` objects, representing the tags contained within the `<body>` tag.
+ `js` - A string containing JavaScript to be run when the page loads. This text is set as the content of a `<script>` tag, which is included in the document if hte value of this field
is not empty
+ `external_js` - A list of strings each corresponding to the name of or filepath to a JavaScript file to be linked to the document. `<script>` tags will be added for each JavaScript file.

## Methods
The following methods may be called on objects of the Document class:
#### Add metadata
```
add_metadata(metadata)
```
Adds a new `<meta>` tag to the document.

*Parameters:*
+ `metadata` - A dictionary with key-value pairs corresponding to the attributes and values of the new meta tag.

#### Remove metadata
```
remove_metadata(attribute, value)
```
Removes a metadata attribute from the document. If this is the only attribute set on its `<meta>` tag, the entire tag is removed. If no attribute-value pair is found matching
the supplied parameters, no action is taken.

*Parameters:*
+ `attribute` - A string representing the name of the meta attribute to remove
+ `value` - The corresponding value of the attribute

#### Add CSS file
```
add_css_file(filename)
```
Links a new CSS file to the document.

*Parameters:*
+ `filename` - A string representing the name of or filepath to the new CSS file.

#### Remove CSS file
```
remove_css_file(filename)
```
Removes the specified CSS file from the document's list of linked CSS files. If the document does not have a CSS file with that name in its list, an `HTMLWriterException` is raised.

*Parameters:*
+ `filename` - A string representing the name of or filepath to the CSS file to remove.

#### Add script file
```
add_script_file(filename)
```
Links a new JavaScript file to the document.

*Parameters:*
+ `filename` - A string representing the name of or filepath to the new JavaScript file.

#### Remove script file
```
remove_script_file(filename)
```
Removes the specified JavaScript file from the document's list of linked JavaScript files. If the document does not have a CSS file with that name in its list,
an `HTMLWriterException` is raised.

*Parameters:*
+ `filename` - A string representing the name of or filepath to the JavaScript file to remove.

#### Get by ID
```
get_by_id(search_id)
```
Mimics the functionality of JavaScript's `document.getElementById()` function. Allows the user to select an element that appears in the document by its HTML ID attribute.
This performs a linear search through the document, starting with the first node and working down, recursing through any nodes contained within each node it searches. As soon as a
node with the matching ID is found, it returns the `Node` object, meaning that if there is more than one node in the document with the same ID, it will return the first one that appears on the page.
If no element with the matching ID is found, `None` is returned.

*Parameters:*
+ `search_id` - A string representing the ID to search for.

#### Get by class name
```
get_by_class_name(class_name)
```
Mimics the functionality of JavaScript's `document.getElementsByClassName()` function, allowing the user to select elements that appear in the document by their HTML class names.
This searches through all nodes in the document, and returns all that have the specified class name as one of its classes. Returns a list of `Node` objects. An empty list is returned
if no nodes match the given class name.

*Parameters:*
+ `class_name` - A string representing the class name to search for.

#### Get by tag name
```
get_by_tag_name(tag_name)
```
Mimics the functionality of JavaScript's `document.getElementsByTagName()` function, allowing the user to select elements that appear in the document by their HTML tag type.
This searches through all nodes in the document, and returns all that are of the specified tag. Returns a list of `Node` objects. An empty list is returned if no matching tags are
found.

*Parameters:*
+ `tag_name` - A string representing the tag name to search for.

#### Insert before
```
insert_before(before_node, insert_node)
```
Mimics the functionality of JavaScript's `document.insertBefore()` function, allowing the user to insert a new node to the document, such that it appears immediately before a specified
existing node. If the specified node to insert before does not exist, a `DOMTreeException` is raised.

*Parameters:*
+ `before_node` - A `Node` object representing a node that is already in the document, before which the new node should be inserted.
+ `insert_node` - A `Node` object that should be inserted into the document.

#### Append child
```
append_child(new_node)
```
Mimics the functionality of JavaScript's `document.appendChild()` function, allowing the user to insert a new node to the end of the document.

*Parameters:*
+ `new_node` - A `Node` object representing the node to append to the document.

#### Remove child
```
remove_child(remove_node)
```
Mimics the functionality of JavaScript's `document.removeChild()` function, allowing the user to remove a child node from the document. If the specified node is not a child of the
node on which the method is called, a `DOMTreeException` is raised.

*Parameters:*
+ `remove_node` - A `Node` object representing the node to remove.

#### Export
```
export(filepath, indent, line_limit)
```
Exports the current document structure to an HTML file, using the following general formatting principles:
+ If the contents of a tag are text, the opening tag, content, and closing tag are all printed on the same line, if it can fit within the line length limit
+ If the contents of a tag are text, but the opening and closing tags along with all the text will not fit on one line, the opening tag, text, and closing tag will each be on
separate lines. The text may be split into multiple lines if necessary to mantain the line length limit.
+ In general, any new tag starts a new line
+ If a tag is an `<a>` tag containing one and only one tag, and the contents of the inner tag, as well as the opening and closing tags for both the anchor tag and the contained tag
all fit on one line, it will be printed on one line.
+ If the contents of a tag are displayed on separate lines from the opening and closing tags, then the contents of a tag are indented one level further than the opening and closing
tags. The number of characters in the total indentation for each line, is factored into the line length when determining if it falls within the line length limit.

*Parameters:*
+ `filepath` - *Optional*. A string representing the name that should be given to the HTML file. This can be specified as a filepath relative to the current working directory.
If left unspecified, defaults to `index.html`
+ `indent` - *Optional*. The sequence of characters (usually some combination of space and/or tab characters) used to represent one level of indentation. If left unspecified, defaults
to four spaces
+ `line_limit` - *Optional*. The number of characters to allow tag content to extend to on a single line, before splitting it into multiple lines. This does not guarantee that every
line will be below the limit, since lines are only split within the content section of a tag. If left unspecified, this limit defaults to 185 characters.