from lld.observer_design_pattern.amazon_notify_me.observable.iphone_observable import IphoneObservable
from lld.observer_design_pattern.amazon_notify_me.observer.email_notification_alert_observer import *
from lld.observer_design_pattern.amazon_notify_me.observer.mobile_notification_alert_observer import *


observable = IphoneObservable()
email_observer1 = EmailNotificationAlertObserver(observable, "shivam1@gmail.com")
# email_observer1.update()
email_observer2 = EmailNotificationAlertObserver(observable, "shivam2@gmail.com")
email_observer3 = EmailNotificationAlertObserver(observable, "shivam3@gmail.com")
mobile_observer1 = MobileNotificationAlertObserver(observable, "900")

observable.add(email_observer1)
observable.add(email_observer2)
observable.add(email_observer3)
observable.add(mobile_observer1)

observable.set_stock_count(10)
