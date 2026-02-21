from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    """Abstract base class defining the core streaming interface."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the stream with a unique identifier."""
        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on optional criteria."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    """Stream handler for environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the sensor stream."""
        super().__init__(stream_id)
        self.count: int = 0
        self.stream_type: str = "Environmental Data"
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of sensor readings."""
        batch_size = len(data_batch)
        self.count += batch_size
        avg_temp = next(
            (item.split(":")[1] for item in data_batch if "temp" in item),
            "N/A"
        )
        return (
            f"Sensor analysis: {batch_size} readings processed, "
            f"avg temp: {avg_temp}°C"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter sensor data by criteria."""
        if criteria == "temp":
            return [item for item in data_batch if "temp" in item]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor stream statistics."""
        return {
            "stream_id": self.stream_id,
            "total_readings": self.count
        }


class TransactionStream(DataStream):
    """Stream handler for financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the transaction stream."""
        super().__init__(stream_id)
        self.count: int = 0
        self.stream_type: str = "Financial Data"
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of financial transactions."""
        batch_size = len(data_batch)
        self.count += batch_size
        buys = sum(
            int(item.split(":")[1])
            for item in data_batch
            if item.startswith("buy")
        )
        sells = sum(
            int(item.split(":")[1])
            for item in data_batch
            if item.startswith("sell")
        )
        net = buys - sells
        net_str = f"+{net}" if net >= 0 else str(net)
        return (
            f"Transaction analysis: {batch_size} operations, "
            f"net flow: {net_str} units"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Filter transaction data by criteria.
        """
        if criteria == "large":
            return [
                item for item in data_batch
                if (item.startswith("buy") or item.startswith("sell"))
                and int(item.split(":")[1]) > 100
            ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction stream statistics."""
        return {
            "stream_id": self.stream_id,
            "total_operations": self.count
        }


class EventStream(DataStream):
    """Stream handler for system event data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the event stream."""
        super().__init__(stream_id)
        self.total_events: int = 0
        self.total_errors: int = 0
        self.stream_type: str = "System Events"
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of system events."""
        batch_size = len(data_batch)
        self.total_events += batch_size
        self.total_errors += len(
            [item for item in data_batch if item == "error"]
        )
        return (
            f"Event analysis: {batch_size} events, "
            f"{self.total_errors} error detected"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event stream statistics."""
        return {
            "stream_id": self.stream_id,
            "total_events": self.total_events,
            "total_errors": self.total_errors
        }


class StreamProcessor:
    """Manages and processes multiple data streams polymorphically."""

    def __init__(self) -> None:
        """Initialize the stream processor with an empty stream list."""
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a stream to the processor."""
        self.streams.append(stream)

    def process_all(self, data_batch: List[Any]) -> List[str]:
        """Process a batch through all registered streams."""
        results = []
        for stream in self.streams:
            try:
                result: str = stream.process_batch(data_batch)
                results.append(result)
            except Exception as e:
                results.append(
                    f"Error processing stream {stream.stream_id}: {e}"
                )
        return results


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_stream = SensorStream("SENSOR_001")
    print("Processing sensor batch: "
          "['temp:22.5', 'humidity:65', 'pressure:1013']")
    print(sensor_stream.process_batch(
        ["temp:22.5", "humidity:65", "pressure:1013"]))
    print()

    transaction_stream = TransactionStream("TRANS_001")
    print("Processing transaction batch: ['buy:100', 'sell:150', 'buy:75']")
    print(transaction_stream.process_batch(["buy:100", "sell:150", "buy:75"]))
    print()

    event_stream = EventStream("EVENT_001")
    print("Processing event batch: ['login', 'error', 'logout']")
    print(event_stream.process_batch(["login", "error", "logout"]))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    batch: List[Any] = [
        "temp:18.0", "temp:21.0",
        "buy:100", "sell:50", "buy:200", "buy:75",
        "login", "error", "logout"
    ]

    results = processor.process_all(batch)

    print("Batch 1 Results:")
    for stream, result in zip(processor.streams, results):
        if isinstance(stream, SensorStream):
            sensor_count = len(
                [x for x in batch if "temp" in x or "humidity" in x]
            )
            print(f"- Sensor data: {sensor_count} readings processed")
        elif isinstance(stream, TransactionStream):
            trans_count = len(
                [x for x in batch
                 if x.startswith("buy") or x.startswith("sell")]
            )
            print(f"- Transaction data: {trans_count} operations processed")
        elif isinstance(stream, EventStream):
            event_count = len(
                [x for x in batch
                 if x in ["login", "logout", "error"]]
            )
            print(f"- Event data: {event_count} events processed")

    print()
    print("Stream filtering active: High-priority data only")

    sensor_filtered = sensor_stream.filter_data(batch, criteria="temp")
    trans_filtered = transaction_stream.filter_data(batch, criteria="large")
    print(
        f"Filtered results: {len(sensor_filtered)} critical sensor alerts, "
        f"{len(trans_filtered)} large transaction"
    )
    print()

    if all("Error" not in r for r in results):
        print("All streams processed successfully. Nexus throughput optimal")
