from lhub_extractors import util

class feature_extractor:
    extractors = {}

    def add_extractor(self, f):
        self.function = f
        self.entrypoint = f"{f.__module__}.{f.__name__}"
        if not self.name:
            self.name = f.__name__
        self.extractors[self.entrypoint] = self

    def __init__(self, name=None):
        self.name = None
        self.function = None
        self.entrypoint = None
        # if the first argument is callable, the first argument is actually the function
        if name and callable(name):
            self.add_extractor(name)
        else:
            self.name = name

    def __call__(self, f, *args, **kwargs):
        if self.function:
            return self.function(f, *args, **kwargs)
        else:
            if not f:
                util.invalid_extractor(
                    code="invalid_extractor",
                    error=f"@feature_extractor: {self.name}  must be called with a function"
                )
            else:
                self.add_extractor(f)
                return f

    @classmethod
    def all(cls):
        return cls.extractors