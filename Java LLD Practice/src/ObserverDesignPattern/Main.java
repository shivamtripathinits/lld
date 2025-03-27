package ObserverDesignPattern;

import ObserverDesignPattern.Observable.IphoneStockObservable;
import ObserverDesignPattern.Observable.StockObservable;
import ObserverDesignPattern.Observer.EmailNotifactionAlertObserver;
import ObserverDesignPattern.Observer.MobileNotifactionAlertObserver;
import ObserverDesignPattern.Observer.NotifactionAlertObserver;

public class Main {
    public static void main(String[] args) {
        StockObservable iphoneStockObservable = new IphoneStockObservable();
        NotifactionAlertObserver mobileNotifactionAlertObserver = new MobileNotifactionAlertObserver("123456789");
        NotifactionAlertObserver emailNotifactionAlertObserver = new EmailNotifactionAlertObserver("xyz@gmail.com");
        iphoneStockObservable.add(mobileNotifactionAlertObserver);
        iphoneStockObservable.add(emailNotifactionAlertObserver);
        iphoneStockObservable.setStock(10);
    }
}
