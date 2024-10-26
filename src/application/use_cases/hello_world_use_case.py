class HelloWorldUseCase:
    def __init__(self, greetings: str = "Hello World"):
        self._greetings = greetings

    def execute(self):
        return {
            "message": self._greetings
        }
