from fbchat import Client
from fbchat.models import*

class Messbot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, 
thread_id=None,thread_type=ThreadType.USER, **kwargs):
        try:
            msg=str(message_object).split(",")[15][14:-1]
            print(msg)
            if("//video.xx.fbcdn" in msg):
                msg=msg
            else:
                msg=str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg=(message_object.text).lower()
                print(msg)
            except:
                pass
#reply to user/send message
    def sendMsg():
        if(author_id != self.uid):
            self.send(Message(text=reply), thread_id=thread_id,
                                thread_type=thread_type)
            if("hi" in msg):
                reply="hello"
                sendMsg()
            elif ("How are you"):
                reply="good"
                sendMsg()
        else:
            pass  
#        sb=SV-JZnj7OzlvHnvXUn4Z;dpr=0.75;wd=1821x809;datr=W1-JZuFAjkYdQmuFqTHP;ps_n=1;ps_l=1;c_user=10004640854172;xs=21%3A1upFyswwrmMg%3A2%3A1720897%3A-1%3A6299%3A%3AAcWZtZfSGGI9U9Gu_uPSMCU6DUZ7MrkBzvDHc2mZUw;presence=C%7B%22l%22%3A%22sc.7269614943126597%22%2C%22t3%22%3A%5B%7B%22o%22%3A0%2C%22i%22%3A%22sc.7003277509769421%22%7D%5D%2C%22utc3%22%3A1720311460785%2C%22v%22%3A1%7D;fr=1z9FSeDqEvEQpOEhW.AWXFGUAUtv2E2BXHxcfe56KQ.Bmid5m..AAA.0.0.Bmid87.AWWj_QaCwTg;
session_cookie={  
    "sb": "SV-JZnj7OzlvHnvXUMxlSn4Z",
    "fr": "1z9FSeDqEvEQpOEhW.AWXFG3yXUAUtv2E2BXHxcfe56KQ.Bmid5m..AAA.0.0.Bmid87.AWWj_QaCwTg",
    "c_user":"100041640854172",
    "datr":"W1-JZuFAjkYdQmvpf4uFqTHP",
    "xs": "21%3A1upFyswGvwrmMg%3A2%3A1720278897%3A-1%3A6299%3A%3AAcWZtZfSGGI9U9Gu_uPSMCU6DUZ7MrkBzvDHc2mZUw"
}      
#bot=Messbot('your email/phone number') #if you user username and password for login
bot=Messbot('','',session_cookies=session_cookie)
print(bot.isLoggedIn())

try:
    bot.listen()
except:
    bot.listen(
