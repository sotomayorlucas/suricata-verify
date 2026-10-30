"""input.pcap: two long-lived modbus connections, 20 marked requests each, every frame in two
TCP segments; the second half of request 6 on 10.128.0.0 is missing (a TCP gap inside a
frame). Uses pcapgen.py in this directory.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pcapgen
pcapgen.generate(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.pcap'),
                 'modbus', 'split', conns=2, transactions=40, lost_request=5)
