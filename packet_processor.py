import sys
import re
from collections import deque

import logging
logging.basicConfig()


class Packet:

    def __init__(self, arrival_time, processing_time):
        self.arrival_time = arrival_time
        self.processing_time = processing_time


class BufferedPacket:

    def __init__(self, start_time, finish_time):
        self.start_time = start_time
        self.finish_time = finish_time

    def __eq__(self, other):
        return self.start_time == other.start_time and self.finish_time == other.finish_time


class PacketProcessor:

    def __init__(self, packets, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = deque(maxlen=buffer_size)
        self.packets = packets
        self.results = []
        self.logger = logging.getLogger('packet_processor')

    def simulate(self):
        start_times = []
        for packet in self.packets:
            self.logger.debug('Packet arriving %s', packet)
            self.drop_processed(packet.arrival_time)
            start_time = self.queue_packet(packet)
            self.logger.debug('Buffer after queueing %s', self.buffer)
            start_times.append(start_time)
        return start_times

    def drop_processed(self, arrival_time):
        if self.buffer:
            packet = self._try_fetch_packet()
            while packet is not None and packet.finish_time <= arrival_time:
                self.buffer.popleft()
                packet = self._try_fetch_packet()

    def queue_packet(self, packet):
        if len(self.buffer) == 0 and self.buffer_size > 0:
            start_time = packet.arrival_time
            self._do_queue(start_time, packet.processing_time)
        elif len(self.buffer) < self.buffer_size:
            start_time = self.buffer[-1].finish_time
            self._do_queue(start_time, packet.processing_time)
        else:
            start_time = -1
        return start_time

    def _do_queue(self, start_time, processing_time):
        finish_time = start_time + processing_time
        buffered_packet = BufferedPacket(start_time=start_time, finish_time=finish_time)
        self.buffer.insert(self.buffer.maxlen, buffered_packet)

    def _try_fetch_packet(self):
        try:
            return self.buffer[0]
        except IndexError:
            return None


if __name__ == '__main__':
    match_object = re.match(r'(\d+)\s(\d+)', sys.stdin.readline().rstrip())
    buffer_size, num_packets = int(match_object.group(1)), int(match_object.group(2))
    packets = []
    for i in range(num_packets):
        match_object = re.match(r'(\d+)\s(\d+)', sys.stdin.readline().rstrip())
        packets.append(Packet(arrival_time=int(match_object.group(1)), processing_time=int(match_object.group(2))))

    pp = PacketProcessor(packets=packets, buffer_size=buffer_size)
    start_times = pp.simulate()
    for st in start_times:
        print(st)


