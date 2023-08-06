from cpython.object cimport PyObject_HasAttr

cdef class CallMetric:
    """
        Average case complexities

        Generally, 'n' is the number of elements currently in the container.
        'k' is either the value of a parameter or the number of elements in the parameter.

        As in:  https://wiki.python.org/moin/TimeComplexity
        TODO: How should this be weighted ? C functions are faster
            The resulting value should be somewhat equivalent to counting bytecode instructions
    """

    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    cdef Py_ssize_t value(self):
        raise NotImplementedError("Must be implemented by subclass.")

cdef class ArgsLengthLinear(CallMetric):
    cdef Py_ssize_t value(self):
        if all(map(lambda x: PyObject_HasAttr(x, '__iter__'), self.args)):
            return sum(map(lambda x: len(x), self.args))
        return len(self.args)

AVG_BUILTIN_FUNCTION_COMPLEXITY = {
    max.__qualname__: ArgsLengthLinear,
    sorted.__qualname__: ArgsLengthLinear,
}
