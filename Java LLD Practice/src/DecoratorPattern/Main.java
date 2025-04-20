package DecoratorPattern;

import DecoratorPattern.BasePizza.BasePizza;
import DecoratorPattern.BasePizza.FarmHouse;
import DecoratorPattern.BasePizza.VegDelight;
import DecoratorPattern.Toppings.CheeseToppings;
import DecoratorPattern.Toppings.MushroomToppings;

public class Main {
    public static void main(String[] args){
        BasePizza basePizza1 = new CheeseToppings(new VegDelight());
        BasePizza basePizza2 = new CheeseToppings(new CheeseToppings(new VegDelight()));
        BasePizza basePizza3 = new MushroomToppings(new FarmHouse());
        System.out.println(basePizza1.cost());
        System.out.println(basePizza2.cost());
        System.out.println(basePizza3.cost());

    }
}
