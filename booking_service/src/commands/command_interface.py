from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        """
        Execute the command
        :return:
        """
