import abc


class ProgramService(abc.ABC):

    @abc.abstractmethod
    def programQuit(self, *args, **kwargs):
        pass
