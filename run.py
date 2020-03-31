"""Main run"""
from src.common.processor_manager import ProcessorManager
from src.writer.writer import WriterProcessor, WriterWorkManager


if __name__ == "__main__":
    write_processor = WriterProcessor()
    write_work_manager = WriterWorkManager(write_processor, 'logs.log')
    processor_manager = ProcessorManager(write_work_manager, num_of_processor=5)

    processor_manager.start()
