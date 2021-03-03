from mycroft import MycroftSkill, intent_file_handler


class ExerciciosNaSemana(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('semana.na.exercicios.intent')
    def handle_semana_na_exercicios(self, message):
        self.speak_dialog('semana.na.exercicios')


def create_skill():
    return ExerciciosNaSemana()

