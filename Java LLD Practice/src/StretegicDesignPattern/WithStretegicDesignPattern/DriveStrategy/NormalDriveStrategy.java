package StretegicDesignPattern.WithStretegicDesignPattern.DriveStrategy;

public class NormalDriveStrategy implements DriveStrategy{
    @Override
    public void drive() {
        System.out.println("Normal Drive");
    }
}
