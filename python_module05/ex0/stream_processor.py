from typing import Any, List
from abc import ABC, abstractmethod


class EmptyError(Exception):
    """Custom exception for empty list/text."""
    pass


class DataProcessor(ABC):
    """DataProcessor Blueprint (Abstract Base Class)."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data: this method marked as rule."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate data: this method marked as rule."""
        pass

    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):
    """NumericProcessor blueprint to process numeric data."""

    def validate(self, numbers_list: Any) -> bool:
        if not numbers_list:
            return False
        for n in numbers_list:
            if not isinstance(n, int):
                raise ValueError(f"'{n}' should be a number.")
        return True

    def process(self, numbers_list: Any) -> str:
        if self.validate(numbers_list):
            total: int = 0
            for n in numbers_list:
                total += n
            length: int = len(numbers_list)
            avg: int = total / length

            return f"Processed {length} numeric values, sum={total}, avg={avg}"

    def format_output(self, result: str) -> str:
        return f"{result}"


class TextProcessor(DataProcessor):
    """TextProcessor blueprint to process text."""

    def validate(self, text: Any) -> bool:
        """Validate text input."""
        if not isinstance(text, str):
            raise ValueError("Text should be string.")
        if len(text) == 0:
            return False
        return True

    def process(self, text: Any) -> str:
        """Process text input."""
        if self.validate(text):
            words: List[str] = text.split()
            word_count: int = len(words)
            return f"{len(text)} characters, {word_count} words"

    def format_output(self, result: str) -> str:
        return f"Processed text: {result}"


class LogProcessor(DataProcessor):
    """NumericProcessor blueprint to process numeric data."""

    def validate(self, log: Any) -> bool:
        is_msg: bool = isinstance(log["message"], str)
        is_type: bool = isinstance(log["type"], str)
        if not is_msg or not is_type:
            raise ValueError("Log entry should be string.")
        if not log["message"] or not log["type"]:
            return False
        return True

    def process(self, log: Any) -> str:
        if self.validate(log):
            if log["type"] == "ERROR":
                return (f"[ALERT] {log['type']} "
                    f"level detected: {log['message']}")
            return (f"[{log['type']}] {log['type']} "
                f"level detected: {log['message']}")

    def format_output(self, result: str) -> str:
        return f"{result}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    numbers_list: List[int] = [1, 2, 3, 4, 5]
    text: str = "Hello Nexus World"
    log: dict[str, str] = {
        "message": "Connection timeout",
        "type": "ERROR"
    }

    try:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {numbers_list}")
        is_valid_list: bool = num_processor.validate(numbers_list)
        if is_valid_list:
            print("Validation: Numeric data verified")
        else:
            raise EmptyError("ERROR: List is empty.")
        n_data_processed: str = num_processor.process(numbers_list)
        n_output: str = num_processor.format_output(n_data_processed)
        print(f"Output: {n_output}")

        print()

        print("Initializing Text Processor...")
        print(f"Processing data: \"{text}\"")
        is_valid_text: bool = text_processor.validate(text)
        if is_valid_text:
            print("Validation: Text data verified")
        else:
            raise EmptyError("Text is empty.")
        t_data_processed: str = text_processor.process(text)
        t_output: str = text_processor.format_output(t_data_processed)
        print(f"Output: {t_output}")

        print()

        print("Initializing Log Processor...")
        print(f"Processing data: \"{log['type']}: {log['message']}\"")
        is_valid_log: bool = log_processor.validate(log)
        if is_valid_log:
            print("Validation: Log entry verified")
        else:
            raise EmptyError("There is no logs.")
        l_data_processed: str = log_processor.process(log)
        l_output: str = log_processor.format_output(l_data_processed)
        print(f"Output: {l_output}")

        print()

        print("=== Polymorphic Processing Demo ===\n")

        numbers_list2: List[int] = [1, 2, 3]
        text2: str = "Hello Nexus!"
        log2: dict[str, str] = {
            "message": "System ready",
            "type": "INFO"
        }

        print("Processing multiple data types through same interface...")
        is_valid_list2: bool = num_processor.validate(numbers_list2)
        if not is_valid_list2:
            raise EmptyError("There is no logs.")
        n_data_processed2: str = num_processor.process(numbers_list2)
        n_output2: str = num_processor.format_output(n_data_processed2)
        print(f"Result 1: {n_output2}")

        is_valid_text2: bool = text_processor.validate(text2)
        if not is_valid_text2:
            raise EmptyError("There is no logs.")
        t_data_processed2: str = text_processor.process(text2)
        t_output2: str = text_processor.format_output(t_data_processed2)
        print(f"Result 2: {t_output2}")

        is_valid_log2: bool = log_processor.validate(log2)
        if not is_valid_log2:
            raise EmptyError("There is no logs.")
        l_data_processed2: str = log_processor.process(log2)
        l_output2: str = log_processor.format_output(l_data_processed2)
        print(f"Result 3: {l_output2}")

        print()

        print("Foundation systems online. Nexus ready for advanced streams")

    except ValueError as e:
        print(f"ERROR: {e}")
    except TypeError:
        print("ERROR: missing arguments 'message' and 'type'.")
    except EmptyError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
