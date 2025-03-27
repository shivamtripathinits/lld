package ObserverDesignPattern.Observable;

import ObserverDesignPattern.Observer.NotifactionAlertObserver;

public interface StockObservable {

    public void add(NotifactionAlertObserver observer);
    public void remove(NotifactionAlertObserver observer);
    public void notifyObserver();
    public void setStock(int stock);
    public void getStock();
}
