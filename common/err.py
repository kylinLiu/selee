class BaseError(Exception):
    error = None
    code = 500

    def __init__(self, err=None):
        self.error = f'{self.__class__.error} {err}'

    def __str__(self):
        return self.error
