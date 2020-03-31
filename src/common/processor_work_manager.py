import abc

class ProcessorWorkManager(abc.ABC):
    """Work manager abstract class"""
    @abc.abstractmethod
    def run(self) -> None:
        """Run work manager"""
        pass

    @abc.abstractmethod
    def stop(self) -> None:
        """Stop work manager"""
        pass