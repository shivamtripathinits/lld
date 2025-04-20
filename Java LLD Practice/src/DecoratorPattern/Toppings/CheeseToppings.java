package DecoratorPattern.Toppings;

import DecoratorPattern.BasePizza.BasePizza;

public class CheeseToppings extends Toppings{

    BasePizza basePizza;
    public CheeseToppings(BasePizza basePizza){
        this.basePizza = basePizza;
    }

    @Override
    public int cost() {
        return this.basePizza.cost() + 20;
    }
}
