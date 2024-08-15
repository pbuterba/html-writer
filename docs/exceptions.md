# Exceptions
The following custom exceptions are exported with this package, and may be used to catch errors according to their usage as documented in this package:

+ `HTMLWriterException` - A general purpose exception used for improper use of functions, or requests to take impossible actions.
+ `NodeTypeException` - An exception that occurs when an operation is attempted on a `Node` object, when the operation is not supported on that particular node type (text, tree, or contentless).
+ `DOMTreeException` - An exception that occurs when a request is made to edit the DOM tree in a way that is impossible given the current state of the DOM tree (e.g. attempting to remove
a node that does not exist in the DOM tree).
+ `AttributeMismatchError` - An exception that occurs when a value is specified for an attribute that does not match the expected type for the attribute.