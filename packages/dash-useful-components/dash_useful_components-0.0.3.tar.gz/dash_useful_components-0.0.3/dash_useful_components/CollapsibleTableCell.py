# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CollapsibleTableCell(Component):
    """A CollapsibleTableCell component.


Keyword arguments:
- index (number; required)
- level (number; optional)"""
    @_explicitize_args
    def __init__(self, index=Component.REQUIRED, onExpand=Component.REQUIRED, level=Component.UNDEFINED, **kwargs):
        self._prop_names = ['index', 'level']
        self._type = 'CollapsibleTableCell'
        self._namespace = 'dash_useful_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['index', 'level']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['index', 'onExpand']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CollapsibleTableCell, self).__init__(**args)
