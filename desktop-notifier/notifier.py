#import the necessary module!
from plyer import notification
#import plyer

#specify the parameters
tittle = 'Hello Amazing people'

message = 'Do suscrib my chanel'

notification.notify(title = tittle, 
                    message = message, 
                    app_icon = None, 
                    timeout=10, 
                    toast = False)
