"""Run writer processor"""
import os
import datetime
import time
import random

from src.common.processor_work_manager import ProcessorWorkManager

class WriterProcessor:
    @staticmethod
    def _format_message(message):
        """Format log message"""
        return f"{datetime.datetime.now()} - {os.getpid()} - {message}\n"

    def process(self, message, filename):
        """Process message"""
        with open(filename, 'a') as f:
            f.write(self._format_message(message))


class WriterWorkManager(ProcessorWorkManager):
    """Writer work manager abstract class"""
    def __init__(self, processor, filename):
        self._processor = processor
        self._filename = filename

    @staticmethod
    def _random_message_generator():
        """Random message generator"""
        num_of_messages = random.randint(0, 1000)
        levels = ['INFO', 'ERROR']
        for i in range(num_of_messages):
            yield f"{levels[random.randint(0, 1)]} - This is my {i}"

    def run(self) -> None:
        """Run work manager"""
        for message in self._random_message_generator():
            self._processor.process(message, self._filename)
        

    def stop(self) -> None:
        """Stop work manager"""
        pass
