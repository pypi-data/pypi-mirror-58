"""List field class & utilities."""
from pofy.loading_context import LoadingContext

from .base_field import BaseField


class ListField(BaseField):
    """List YAML object field."""

    def __init__(self, item_field: BaseField, *args, **kwargs):
        """Initialize the list field.

        Arg:
            item_field: Field used to load list items.
            *args, **kwargs: Arguments forwarded to BaseField.

        """
        super().__init__(*args, **kwargs)
        self._item_field = item_field

    def _load(self, context: LoadingContext):
        if not context.expect_sequence():
            return None

        node = context.current_node()
        result = []
        for item_node in node.value:
            with context.load(item_node) as loaded:
                if not loaded:
                    continue

                item = self._item_field.load(context)
                result.append(item)

        return result
