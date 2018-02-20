#First try of a random ruthe-cartoon-module

import random

from FaustBot.Communication import Connection
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype

class RutheObserver(PrivMsgObserverPrototype):
    @staticmethod
    def cmd():
        return [".ruthe"]

    @staticmethod
    def help():
        return ".ruthe - Gibt einen Ruthe-Cartoon aus."

    def update_on_priv_msg(self, data: dict, connection: Connection):
        if data['message'].find('.ruthe') == -1:
            return
        cartoonnumber = str(random.randint(1, 3164))
        connection.send_back('\001ACTION liefert ' + data['nick'] + ' einen Ruthe-Cartoon: http://ruthe.de/cartoon/' + cartoonnumber + '/ .\001', data)
