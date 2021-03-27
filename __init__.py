from mycroft import MycroftSkill, intent_file_handler


class Lyrics(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lyrics.intent')
    def handle_lyrics(self, message):
        song = message.data.get('song')

        self.speak_dialog('lyrics', data={
            'song': song
        })


def create_skill():
    return Lyrics()

