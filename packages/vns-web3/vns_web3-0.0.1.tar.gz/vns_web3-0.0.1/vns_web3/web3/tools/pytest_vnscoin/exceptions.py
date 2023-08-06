class PytestVnscoinError(Exception):
    """
    Base class for all Pytest-Vnscoin errors.
    """

    pass


class DeployerError(PytestVnscoinError):
    """
    Raised when the Deployer is unable to deploy a contract type.
    """

    pass


class LinkerError(PytestVnscoinError):
    """
    Raised when the Linker is unable to link two contract types.
    """

    pass
