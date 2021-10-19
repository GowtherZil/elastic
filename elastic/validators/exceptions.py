class ValidationError(Exception):
    def __init__(self, errors: list[str], *args: object) -> None:
        super().__init__(*args)
        self._errors = errors

    @property
    def errors(self):
        return self._errors
