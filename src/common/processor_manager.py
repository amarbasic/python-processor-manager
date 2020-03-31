import logging
from multiprocessing import Process

from .processor_worker import ProcessorWorker
from .processor_work_manager import ProcessorWorkManager

class ProcessorManager:
    """Processor manager"""

    def __init__(self, processor_work_manager: ProcessorWorkManager, num_of_processor: int):
        self._num_of_processor = num_of_processor
        self._processes = []
        self._processor_workers = []

        for index in range(num_of_processor):
            processor_worker = ProcessorWorker(processor_work_manager)
            processor = Process(target=self._work, args=(index,))
            self._processor_workers.append(processor_worker)
            self._processes.append(processor)

    def _work(self, index):
        """Run work"""
        worker = self._processor_workers[index]
        worker.run()

    def start(self):
        """Start processes"""
        for process in self._processes:
            logging.info("Start process: %s", process)
            process.start()

    def stop(self):
        """Stop processes"""
        for processor_worker in self._processor_workers:
            processor_worker.join()

        for process in self._processes:
            process.join()