"""Resolvers class & utilities.

Resolvers are used when an !include tag is encountered, to load the included
YAML documents.
"""
from abc import abstractmethod
from re import compile as re_compile

from yaml import Node


class TagHandler:
    """Abstract class used to transform yaml node when a tag is encountered.

    Members:
        tag_pattern: The tag pattern for this handler, without leading !
    """

    tag_pattern: str = None

    def __init__(self):
        """Initialize TagHandler."""
        self._compiled_pattern = re_compile(self.tag_pattern)

    def match(self, node: Node) -> bool:
        """Check if this handler matches the tag on the given node.

        Args:
            node: The node on which the tag to test is defined.

        """
        assert node.tag is not None
        assert node.tag[0] == '!'  # Only handle custom tags.

        pattern = self._compiled_pattern
        tag = node.tag[1:]  # Remove !

        return pattern.match(tag) is not None

    @abstractmethod
    def transform(self, context) -> Node:
        """Transform the given node.

        Args:
            context: The loading context.

        Return:
            The transformed node (loaded yaml file, environment variable....)

        """
