


class BadBoyError(Exception):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(BadBoyError):
    ...
