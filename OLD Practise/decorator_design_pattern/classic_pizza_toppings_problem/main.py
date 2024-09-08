from lld.decorator_design_pattern.classic_pizza_toppings_problem.base.veg_base import VegBase
from lld.decorator_design_pattern.classic_pizza_toppings_problem.base.non_veg_base import NonVegBase
from lld.decorator_design_pattern.classic_pizza_toppings_problem.toppings.cheese import CheeseToppings
from lld.decorator_design_pattern.classic_pizza_toppings_problem.toppings.corn import CornToppings
from lld.decorator_design_pattern.classic_pizza_toppings_problem.toppings.paneer import PaneerToppings


veg_base = VegBase()
non_veg_base = NonVegBase()

print("Cost for veg and non veg base is {} and {} resp ".format(veg_base.cost(), non_veg_base.cost()))

cheese_topping = CheeseToppings(veg_base)
paneer_topping = PaneerToppings(veg_base)
corn_topping = CornToppings(veg_base)


print("veg base with cheese toppings cost is ", cheese_topping.cost())

print("non veg base with cheese toppings and corn toppings cost is ",
      CornToppings(CheeseToppings(NonVegBase())).cost())

