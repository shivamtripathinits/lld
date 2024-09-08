from lld.decorator_design_pattern.classic_pizza_toppings_problem.decorator.decorator_base import DecoratorBase


class CornToppings(DecoratorBase):
    def __init__(self, base_pizza):
        self.base_pizza = base_pizza

    def cost(self):
        return self.base_pizza.cost() + 20

