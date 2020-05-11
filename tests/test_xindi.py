#!/usr/bin/env python

from xindi import ManagedNetwork

input_data = dict()
input_data['managed_network'] = '10.0.0.0/26'

my_first_net = dict(usecase='first network', owner='Wolfgang Wangerin', department='ITA')
my_second_net = dict(usecase='second network', owner='Count Duckula', department='OTI')

managed_network = ManagedNetwork(indict=input_data)
managed_network.next_free_subnet(27, my_first_net)
managed_network.next_free_subnet(27, my_second_net)
managed_network.free('10.0.0.0/27')
assert(
    managed_network.export() == {
        'assigned_subnets': [{'cidr': '10.0.0.32/27',
        'department': 'OTI',
        'owner': 'Count Duckula',
        'usecase': 'second network'}],
        'managed_network': '10.0.0.0/26'
        }
)
