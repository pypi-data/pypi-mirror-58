# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TreeTableRow(Component):
    """A TreeTableRow component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): Children (rowcells)
- id (string; optional): The ID used to identify this component in Dash callbacks
- height (number; optional): The node value"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, height=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'height']
        self._type = 'TreeTableRow'
        self._namespace = 'dash_useful_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'height']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(TreeTableRow, self).__init__(children=children, **args)
