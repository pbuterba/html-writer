"""
@package    htmlwriter
@brief      Contains custom exceptions to be used in the package

@date       8/3/2024
@updated    8/17/2024

@author     Preston Buterbaugh
"""


class HTMLWriterException(Exception):
    """
    @brief  General exception to be used by the HTML writer
    """
    pass


class NodeTypeException(Exception):
    """
    @brief  Exception for a mismatch between expected and actual node types (text, tree, or self-closing tag)
    """
    pass


class DOMTreeException(Exception):
    """
    @brief  An exception for unexpected conditions in a DOM tree
    """
    pass


class AttributeTypeMismatch(Exception):
    """
    @brief  An exception for when attributes are set to values of the wrong type
    """
    pass
