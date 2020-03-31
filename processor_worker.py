from .processor_work_manager import ProcessorWorkManager

class ProcessorWorker:
    """Process worker class"""

    def __init__(self, processor_work_manager: ProcessorWorkManager):
        self._running = True
        self.processor_work_manager = processor_work_manager

    def run(self):
        """Run worker"""
        while self._running:
            try:
                self.process()
            except Exception:
                logging.error(traceback.format_exception(*sys.exc_info()))
                continue

    def process(self):
        """Call process on queue"""
        self.processor_work_manager.run()

    def join(self):
        """Join processes"""
        self._running = False