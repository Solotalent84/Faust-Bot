import random

from FaustBot.Communication import Connection
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype

class TestObserver(PrivMsgObserverPrototype):
    @staticmethod
    def cmd():
        return [".test"]

    @staticmethod
    def help():
        return ".test - Test ist ein Testmodul"

    def update_on_priv_msg(self, data: dict, connection: Connection):
        if data['message'].find('.test') == -1:
            return
        cartoonnumber = str(random.randint(1, 3164))
        connection.send_back('\001ACTION zeigt ' + data['nick'] + ' Bilder von Ameisen: https://www.google.de/search?q=ameisen&tbm=isch .\001', data)
