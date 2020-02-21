
class Game:

    def __init__(self, speech_to_text, input_data, presentation):
        self.speech_to_text = speech_to_text
        self.input_data = input_data
        self.presentation = presentation
        self.reset()

    def reset(self):
        self.points = 0
        self.time = 0
        self.questions = 0

    def play_game(self):
        try:
            while not self.presentation.exit:
                self._play_round()
        except KeyboardInterrupt:
            self.presentation.shutdown()

    def _play_round(self):
        text = self.input_data.get_text()
        self.presentation.print_question(text)
        responce, error, time = self.speech_to_text.get_response()
        if error:
            self.presentation.print_error(error)
            return

        self.questions += 1
        self.time = self.time + time
        is_ok = self._is_ok(text, responce)
        self.points = self.points + 1 if is_ok else self.points
        self.presentation.update_points(self.points, is_ok)
        self.presentation.update_time("%.3f" % (self.time/self.questions))

    @staticmethod
    def _is_ok(text, responce):
        return text in responce
