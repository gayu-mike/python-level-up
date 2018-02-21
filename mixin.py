class Mixin:
    """Mixin class"""
    def __str__(self):
        self.__visited = {}
        return '<Instance of {}, address {}:\n{}{}>'.format(
            self.__class__.__name__,
            id(self),
            self.__attrs(self, 0),
            self.__clss(self.__class__, 4)
        )

    def __attrs(self, ins, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(ins.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{}\n'.format(attr)
            else:
                result += spaces + '{}={}\n'.format(attr, getattr(self, attr))
        return result

    def __clss(self, cls, indent):
        dots = '.' * indent
        if cls in self.__visited:
            return '\n{}<Class {}: address {}>\n'.format(
                dots,
                cls.__name__,
                id(cls)
            )
        else:
            self.__visited[cls] = True
            gen_above = (self.__clss(c, indent + 4) for c in cls.__bases__)
            return '\n{}<Class {}: address {}:\n{}{}{}>\n'.format(
                dots,
                cls.__name__,
                id(cls),
                self.__attrs(cls, indent),
                ''.join(gen_above),
                dots
            )
