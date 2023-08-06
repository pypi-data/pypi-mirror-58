class Base(object):
    @staticmethod
    def _check_input(name, x, cls):
        if not isinstance(x, cls):
            raise TypeError(
                f"`{name}` must be of type {cls.__name__}."
                )

    def __repr__(self):
        items = (f"{i.strip('_')}={vars(self)[i]!r}" for i in vars(self))
        return f"{self.__class__.__name__}({', '.join(items)})"


def option(character, instruction, newline=True):
    if newline:
        return f"[{character}] {instruction}  \n"
    return f"[{character}] {instruction}"


def docstring_parameter(*args, **kwargs):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*args, **kwargs)
        return obj
    return dec
