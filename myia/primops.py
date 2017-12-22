"""Primitive operations.

Primitive operations are handled as constants in the intermediate
representation, with the constant's value being an instance of a `Primitive`
subclass.

"""


class Primitive:
    """Base class for primitives."""

    def __str__(self) -> str:
        """Return a string representation of the primitive.

        By default a lower case version of the class name will be returned e.g.
        `add`, `return`, etc.

        """
        return self.__class__.__name__.lower()


class Add(Primitive):
    """Scalar addition."""

    pass


class If(Primitive):
    """An if-else expression.

    This is a special primitive which takes 3 values: A boolean and two
    anonymous functions without parameters (thunks). This primitive will
    execute one of the two functions, depending on the boolean value, and
    return the result.

    """

    pass


class Return(Primitive):
    """Return primtive.

    Each function must end with a call to this primitive, the arguments to
    which will be the values returned by the function.

    """

    pass