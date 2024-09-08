from lld.factory_pattern.square import Square
from lld.factory_pattern.rectangle import Rectangle


class FactoryShapeDraw:
    def __init__(self, shape):
        self.shape = shape

    def get_shape(self):
        if self.shape == 'rec':
            return Rectangle()
        if self.shape == "squ":
            return Square()
        return None
