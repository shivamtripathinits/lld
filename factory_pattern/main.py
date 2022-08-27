from lld.factory_pattern.factory_class import FactoryShapeDraw

shape = FactoryShapeDraw("rec")
shape_aquired = shape.get_shape()
shape_aquired.draw()


shape = FactoryShapeDraw("squ")
shape_aquired = shape.get_shape()
shape_aquired.draw()

