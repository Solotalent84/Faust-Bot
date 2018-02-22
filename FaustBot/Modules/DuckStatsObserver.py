from FaustBot.Communication import Connection
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype


class DuckStatsObserver(PrivMsgObserverPrototype):
    @staticmethod
    def cmd():
        return [".duckstats"]

    @staticmethod
    def help():
        return ".duckstats - Gibt dem User seine Enten/Abschüsse aus."

    def update_on_priv_msg(self, data: dict, connection: Connection):
        if data['message'].find('.duckstats') == -1:
            return
        connection.send_channel(
            data['nick'] + " hat schon " + str(self.ducks_befriend[data['nick']]) + " befreundete Enten und " + str(
                self.ducks_hunt[data['nick']]) + " getötete Enten.")
