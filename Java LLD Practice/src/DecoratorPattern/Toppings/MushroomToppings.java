package DecoratorPattern.Toppings;

import DecoratorPattern.BasePizza.BasePizza;

public class MushroomToppings extends Toppings{
    BasePizza basePizza;
    public MushroomToppings(BasePizza basePizza){
        this.basePizza = basePizza;
    }

    @Override
    public int cost() {
        return this.basePizza.cost()+30;
    }
}
