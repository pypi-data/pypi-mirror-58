import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.show_l2route import ShowL2routeEvpnMac,\
                                                ShowL2routeEvpnMacEvi
                                                
# ==========================
#  show l2route evpn mac all
#  show l2route evpn mac evi <evi>
# ==========================
class test_show_l2route_evpn_mac(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''
        N95_1# sh l2route evpn mac all

        Flags -(Rmac):Router MAC (Stt):Static (L):Local (R):Remote (V):vPC link 
        (Dup):Duplicate (Spl):Split (Rcv):Recv (AD):Auto-Delete (D):Del Pending
        (S):Stale (C):Clear, (Ps):Peer Sync (O):Re-Originated (Nho):NH-Override
        (Pf):Permanently-Frozen

        Topology    Mac Address    Prod   Flags         Seq No     Next-Hops      
        ----------- -------------- ------ ------------- ---------- ----------------
        100         fa16.3e59.d0b2 BGP    SplRcv        0          10.166.1.1       
        100         fa16.3ec1.a96f Local  L,            0          Eth1/4         
        1000        5e01.8002.0007 VXLAN  Rmac          0          10.166.1.1     
    '''}

    golden_parsed_output = {
        'topology':
            {'100':
                {'mac_address':
                    {'fa16.3e59.d0b2':
                        {'flags': 'SplRcv',
                         'next_hops': '10.166.1.1',
                         'prod': 'BGP',
                         'seq_no': '0'},
                     'fa16.3ec1.a96f':
                        {'flags': 'L,',
                         'next_hops': 'Eth1/4',
                         'prod': 'Local',
                         'seq_no': '0'}}},
             '1000':
                {'mac_address':
                    {'5e01.8002.0007':
                        {'flags': 'Rmac',
                         'next_hops': '10.166.1.1',
                         'prod': 'VXLAN',
                         'seq_no': '0'}
                    }
                }
            }
        }

    golden_parsed_output_evi = {
        'topology': {
            '101': {
                'mac_address': {
                    'fa16.3e04.e54a': {
                        'prod': 'BGP',
                        'flags': 'Spl',
                        'seq_no': '0',
                        'next_hops': '10.84.66.66',
                        },
                    'fa16.3e79.6bfe': {
                        'prod': 'Local',
                        'flags': 'L,',
                        'seq_no': '0',
                        'next_hops': 'Eth1/4',
                        },
                    'fa16.3e9a.e558': {
                        'prod': 'BGP',
                        'flags': 'Spl',
                        'seq_no': '0',
                        'next_hops': '10.84.66.66',
                        },
                    'fa16.3ec5.fcab': {
                        'prod': 'Local',
                        'flags': 'L,',
                        'seq_no': '0',
                        'next_hops': 'Po1',
                        },
                    'fa16.3ed1.37b5': {
                        'prod': 'Local',
                        'flags': 'L,',
                        'seq_no': '0',
                        'next_hops': 'Po1',
                        },
                    'fa16.3ed4.83e4': {
                        'prod': 'Local',
                        'flags': 'L,',
                        'seq_no': '0',
                        'next_hops': 'Eth1/3',
                        },
                    },
                },
            },
        }

    golden_output_evi = {'execute.return_value': '''
        R2# show l2route evpn mac evi 101

        Flags -(Rmac):Router MAC (Stt):Static (L):Local (R):Remote (V):vPC link 
        (Dup):Duplicate (Spl):Split (Rcv):Recv (AD):Auto-Delete (D):Del Pending
        (S):Stale (C):Clear, (Ps):Peer Sync (O):Re-Originated (Nho):NH-Override
        (Pf):Permanently-Frozen

        Topology    Mac Address    Prod   Flags         Seq No     Next-Hops      
        ----------- -------------- ------ ------------- ---------- ----------------
        101         fa16.3e04.e54a BGP    Spl           0          10.84.66.66    
        101         fa16.3e79.6bfe Local  L,            0          Eth1/4         
        101         fa16.3e9a.e558 BGP    Spl           0          10.84.66.66    
        101         fa16.3ec5.fcab Local  L,            0          Po1            
        101         fa16.3ed1.37b5 Local  L,            0          Po1            
        101         fa16.3ed4.83e4 Local  L,            0          Eth1/3      
    '''}

    def test_show_l2route_evpn_mac(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2routeEvpnMac(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_l2route_evpn_mac_evi(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_evi)
        obj = ShowL2routeEvpnMac(device=self.device)
        parsed_output = obj.parse(evi=101)
        self.assertEqual(parsed_output, self.golden_parsed_output_evi)

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeEvpnMac(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ============================================
#  show l2route evpn mac evi <WORD> mac <WORD>
# ============================================
class test_show_l2route_evpn_mac_evi(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''
        CH-P2-TOR-1# sh l2route evpn mac evi 1001  mac 0000.04b1.0000

        Flags -(Rmac):Router MAC (Stt):Static (L):Local (R):Remote (V):vPC link 
        (Dup):Duplicate (Spl):Split (Rcv):Recv (AD):Auto-Delete (D):Del Pending
        (S):Stale (C):Clear, (Ps):Peer Sync (O):Re-Originated (Nho):NH-Override
        (Pf):Permanently-Frozen

        Topology    Mac Address    Prod   Flags         Seq No     Next-Hops      
        ----------- -------------- ------ ------------- ---------- ----------------
        1001        0000.04b1.0000 BGP    SplRcv        19         10.9.0.101        
    '''}

    golden_parsed_output = {'topology':
                            {'1001':
                                {'mac_address':
                                    {'0000.04b1.0000':
                                        {'flags': 'SplRcv',
                                         'next_hops': '10.9.0.101',
                                         'prod': 'BGP',
                                         'seq_no': '19'}
                                        }
                                    }
                                }
                            }

    golden_output_1 = {'execute.return_value': '''
        CH-P2-TOR-1# sh l2route evpn mac evi 1001  mac 0000.0191.0000

        Flags -(Rmac):Router MAC (Stt):Static (L):Local (R):Remote (V):vPC link 
        (Dup):Duplicate (Spl):Split (Rcv):Recv (AD):Auto-Delete (D):Del Pending
        (S):Stale (C):Clear, (Ps):Peer Sync (O):Re-Originated (Nho):NH-Override
        (Pf):Permanently-Frozen

        Topology    Mac Address    Prod   Flags         Seq No     Next-Hops      
        ----------- -------------- ------ ------------- ---------- ----------------
        1001        0000.0191.0000 Local  L,            1          Eth1/11        
        CH-P2-TOR-1#       
    '''}

    golden_parsed_output_1 = {'topology':
                                {'1001':
                                    {'mac_address':
                                        {'0000.0191.0000':
                                            {'prod': 'Local',
                                             'flags': 'L,',
                                             'next_hops':'Eth1/11',
                                             'seq_no': '1'}
                                        }
                                    }
                                }
                            }

    def test_show_l2route_evpn_mac(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2routeEvpnMacEvi(device=self.device)
        parsed_output = obj.parse(evi='1001', mac='0000.04b1.0000')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_l2route_evpn_mac_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowL2routeEvpnMacEvi(device=self.device)
        parsed_output = obj.parse(evi='1001', mac='0000.0191.0000')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2routeEvpnMacEvi(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(evi='1001', mac='0000.04b1.0000')

if __name__ == '__main__':
    unittest.main()