from fixed_queue import FixedQueue

from operator import itemgetter
from dataclasses import dataclass

@dataclass
class Packet:
    arrival_time: int
    processing_time: int

@dataclass
class BufferedPacket:
    start_time: int
    finish_time: int


class PacketProcessor:

    def __init__(self, packets, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = FixedQueue(length=self.buffer_size)
        self.packets = packets
        self.results = []

    def simulate(self):
        start_times = []
        for packet in self.packets:
            self.drop_processed(packet.arrival_time)
            print('Packet arriving', packet)
            print('Buffer after dropping', self.buffer)
            start_time = self.queue_packet(packet)
            print('Buffer after queueing', self.buffer)
            start_times.append(start_time)
        return start_times

    def drop_processed(self, arrival_time):
        if not self.buffer.is_empty():
            packet = self.buffer.top()
            while packet is not None and packet.finish_time <= arrival_time:
                _ = self.buffer.dequeue()
                packet = self.buffer.top()

    def queue_packet(self, packet):
        if self.buffer.is_empty():
            start_time = packet.arrival_time
            self._do_queue(start_time, packet.processing_time)
        elif not self.buffer.is_full():
            start_time = self.buffer.last_item().finish_time
            self._do_queue(start_time, packet.processing_time)
        else:
            start_time = -1
        return start_time

    def _do_queue(self, start_time, processing_time):
        finish_time = start_time + processing_time
        buffered_packet = BufferedPacket(start_time=start_time, finish_time=finish_time)
        self.buffer.enqueue(buffered_packet)
