package ObserverDesignPattern.Observable;

import ObserverDesignPattern.Observer.NotifactionAlertObserver;

import java.util.ArrayList;

public class IphoneStockObservable implements StockObservable{

    public ArrayList<NotifactionAlertObserver> observerList = new ArrayList<NotifactionAlertObserver>();
    int stockCount = 0;
    @Override
    public void add(NotifactionAlertObserver observer) {
        observerList.add(observer);
    }

    @Override
    public void remove(NotifactionAlertObserver observer) {
        observerList.remove(observer);
    }

    @Override
    public void notifyObserver() {
        for(NotifactionAlertObserver observer: observerList){
            observer.notifySubs();
        }
    }

    @Override
    public void setStock(int stock) {
        stockCount = stockCount + stock;
        notifyObserver();
    }

    @Override
    public void getStock() {
        System.out.println(stockCount);
    }
}
