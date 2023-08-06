from ...core import Nexus


class NexusCostFunctionError(Exception):
    pass


class NexusCostFunctionWithFallbacks(object):

    def __init__(self, func_and_fallbacks, dependencies={}):
        self._funcs = func_and_fallbacks
        self._deps = dependencies

    def bind(self, nexus):
        # todo: check nexus
        for _dep_key, _dep in self._deps.items():
            # string values indicate aliases
            if isinstance(_dep, str):
                nexus.new_alias(**{_dep_key: _dep})

            # callable handles indicate component functions
            elif callable(_dep):
                nexus.new_function(_dep, function_name=_dep_key, wire_parameters=False)

            # add simple node
            else:
                nexus.new(**{_dep_key: _dep})

        for _f in self._funcs:
            nexus.new_function(_f)

    def eval(self, nexus):
        for _f in self._funcs:
            try:
                return nexus.get(_f.__name__).value
            except:
                pass  # function failed; try next
        return np.inf  # all function variants threw exception



class NexusCostFunction(CostFunctionWithFallbacks):

    def __init__(self, func, dependencies={}):
        super(CostFunction, self).__init__(
            func_and_fallbacks=(func,),
            dependencies=dependencies
        )


###

from ...core import Nexus


_OPERATORS = {
    # arithmetic
    'add': operator.add,
    'sub': operator.sub,
    'mul': operator.mul,
    'truediv': operator.truediv,
    'floordiv': operator.floordiv,
    'mod': operator.mod,
}

# 'div' operator only available in Python 2
if six.PY2:
    _OPERATORS['div'] = operator.div

def _add_operators(cls):
    """class decorator for implementing common operator methods"""

    for name, op in list(_OPERATORS.items()):
        setattr(cls, '__{}__'.format(name), cls._make_binop_method(op))

    return cls


class CostTriggerFallbackException(Exception):
    """raised inside a cost function to indicate that fallback should be returned instead"""
    pass

@_add_operators
class CostFunction(object):
    def __init__(self, func, dependencies={}, parameter_names=None):
        try:
            iter(func)
        except:
            self._func = (func,)
        else:
            self._func = func

        self._name = '_'.join([_f.__name__ for _f in self._func])
        self._parameter_names = parameter_names
        self._deps = dependencies
        self._nexus = None

    @classmethod
    def _make_binop_method(cls, op):
        def _op_method(self, other):
            _outer_func = lambda *args: op(*args)
            _outer_func.__name__ = "{}__{}__{}".format(self._name, op.__name__, other._name)

            # detect incompatible dependencies
            _incompatible_keys = []
            for _k in self._deps:
                if _k in other._deps and other._deps[_k] != self._deps[_k]:
                    _incompatible_keys.append(_k, self._deps[_k], other._deps[_k])
            if _incompatible_keys:
                _err = "Cannot create composite cost function:" + '\n '.join([
                    "Dependency '{}' declared differently in operands ({} != {}).".format(*_ike)
                    for _ike in _incompatible_keys
                ])
                raise ValueError(_err)

            return CostFunction(
                _outer_func,
                dependencies=dict(
                    self._deps,
                    **dict(other._deps, **{self._name: self, other._name: other})
                ),
                parameter_names=[self._name, other._name]
            )

        return _op_method

    def onfail(self, other):
        _outer_func = lambda *args: op(*args)
        _outer_func.__name__ = "{}__{}__{}".format(self._name, op.__name__, other._name)

        # detect incompatible dependencies
        _incompatible_keys = []
        for _k in self._deps:
            if _k in other._deps and other._deps[_k] != self._deps[_k]:
                _incompatible_keys.append(_k, self._deps[_k], other._deps[_k])
        if _incompatible_keys:
            _err = "Cannot create composite cost function:" + '\n '.join([
                "Dependency '{}' declared differently in operands ({} != {}).".format(*_ike)
                for _ike in _incompatible_keys
            ])
            raise ValueError(_err)

        return CostFunction(
            _outer_func,
            dependencies=dict(
                self._deps,
                **dict(other._deps, **{self._name: self, other._name: other})
            ),
            parameter_names=[self._name, other._name]
        )

    def bind(self, nexus):
        if self._nexus is not None:
            raise ValueError("Cannot rebind!")
        # todo: check nexus
        for _dep_key, _dep in self._deps.items():
            # string values indicate aliases
            if isinstance(_dep, str):
                nexus.new_alias(**{_dep_key: _dep})
            # dict for more complex cases
            elif isinstance(_dep, dict):
                _fn = _dep.get('function_name', None) or _dep_key
                _pn = _dep.get('parameters_names', None)
                nexus.new_function(
                    _dep,
                    function_name=_fn,
                    wire_parameters=False)
                if _pn:
                    nexus.get(_fn).set_parameter_values(_pn)
            # dependent CostFunctions -> call `bind`
            elif isinstance(_dep, CostFunction):
                _dep.bind(nexus)
            # callable handles indicate component functions
            elif callable(_dep):
                #nexus.new_function(_dep, function_name=_dep_key)
                nexus.new_function(_dep, function_name=_dep_key, wire_parameters=False)
            # error
            else:
                raise ValueError("Need string or callable!")

        for _f in self._func:
            #nexus.new_function(_f, wire_parameters=False)
            nexus.new_function(_f, function_name=self._name)
            _node = nexus.get(self._name)
            if self._parameter_names:
                _node.parameter_names = self._parameter_names

        self._nexus = nexus

    def __call__(self):
        return self.eval(self._nexus)

    def eval(self, nexus):
        for _f in self._func:
            try:
                return nexus.get(_f.__name__).value
            except CostTriggerFallbackException:
                pass  # function failed; try next
        return np.inf  # all function variants threw exception
