class Entity:
    @property
    def attributes(self):
        return tuple(vars(self).values())