from queue import FixedQueue

from operator import itemgetter

class PacketProcessor:

    def __init__(self, packets, buffer_size):
        self.buffer = FixedQueue(length=buffer_size)
        self.buffer_last_finish = 0
        self.packets = packets
        self.results = []


    def simulate(self):
        for packet in packets:
            arrival_time, _ = packet
            self.drop_processed(arrival_time)
            self.queue_packet(packet)

    def drop_processed(self, arrival_time):
        if not self.buffer.is_empty():
            _, finish_time = self.buffer.pop()
            while finish_time < arrival_time:
                _, finish_time = self.buffer.pop()

    def queue_packet(self, packet):
        if self.buffer.is_empty():
            arrival_time, processing_time = packet
            start_time = arrival_time
        elif not self.buffer.is_full():
