from mycroft import MycroftSkill, intent_file_handler


class Simplenote(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('simplenote.intent')
    def handle_simplenote(self, message):
        self.speak_dialog('simplenote')


def create_skill():
    return Simplenote()

