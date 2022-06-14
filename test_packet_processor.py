import pytest
from unittest.mock import Mock

from packet_processor import PacketProcessor, Packet, BufferedPacket
from collections import deque


def test_drop_processed():
    pp = PacketProcessor(packets=Mock(), buffer_size=3)
    pp.buffer = deque([BufferedPacket(0, 2),  BufferedPacket(2, 3)])
    pp.drop_processed(arrival_time=2)
    exp_top = BufferedPacket(2, 3)
    exp_buffer = deque([exp_top])
    assert pp.buffer == exp_buffer


@pytest.mark.parametrize(('packets', 'buffer_size', 'exp_results'),
                         [
                             ([(0, 1), (1, 3), (2, 1), (2, 1)], 2, [0, 1, 4, -1]),
                             ([], 2, []),
                             ([(0, 0)], 2, [0]),
                             ([(0, 1), (0, 1)], 1, [0, -1]),
                             ([(0, 1), (1, 1)], 1, [0, 1])
                         ])
def test_simulate(packets, buffer_size, exp_results):
    packets = [Packet(*pkt) for pkt in packets]
    pp = PacketProcessor(packets=packets, buffer_size=buffer_size)
    assert pp.simulate() == exp_results
