# HTML Writer
This package provides convenient Python functions for creating an HTML page. Instead of writing the necessary text data to a file using Python's file writing utilities, you can
build an HTML document structure as a Python object, before exporting it and letting the actual syntax be filled in automatically. Many functions are designed to mimic exiting DOM
manipulation functions from JavaScript.

## Setup and usage
Clone this GitHub repo into your project (you can set it up as a submodule, if your project is in its own Git repository). Objects can then be imported using code similar to below:
```
from htmlwriter import Document
```
The following objects are available to import, each with their own [documentation](docs) available:
+ [`Document`](docs/document.md)
+ [`Doctype`](docs/doctype.md)
+ [`Node`](docs/node.md)

Additionally, several [exceptions](docs/exceptions.md) are included in the package which can be imported and caught in try-except statements where necessary:
+ `HTMLWriterException`
+ `NodeTypeException`
+ `DOMTreeException`
+ `AttributeTypeMismatch`

## Limitations
The package is currently only set up to write HTML. Any internal CSS or JavaScript supplied will be written into the HTML file in exactly the format it is given, with no additional
line breaks, indentation, or spacing. The HTML writer does not perform any sanity checking on the specified HTML document to ensure that it is valid HTML. For example, a "src" attribute
could be set on a `<p>` tag, when that attribute has no meaning for that tag, or a non-existent attribute may even be set. This utility merely provides a convenient way to
programmatically generate HTML, and does not provide any sort of check on the quality of the code.

## Changelog
+ v.1.0.1 - December 20th, 2024
  + Fixed critical bug with `get_by_class_name()` function
  + Added check for unencodable characters when exporting HTML files, now replaced by "?" character
+ v.1.0.0 - August 17th, 2024
  + Initial release