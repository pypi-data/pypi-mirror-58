# This file is part of the TREZOR project.
#
# Copyright (C) 2012-2016 Marek Palatinus <slush@satoshilabs.com>
# Copyright (C) 2012-2016 Pavol Rusnak <stick@satoshilabs.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.
#
# The script has been modified for KeepKey Device.

import unittest
import common
import binascii
import itertools

import keepkeylib.messages_pb2 as proto
import keepkeylib.types_pb2 as proto_types
from keepkeylib.client import CallException
from keepkeylib import tx_api

class TestOpReturn(common.KeepKeyTest):

    def test_opreturn(self):
        self.setup_mnemonic_nopin_nopassphrase()

        # tx: d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882
        # input 0: 0.0039 BTC

        inp1 = proto_types.TxInputType(address_n=[0],  # 14LmW5k4ssUrtbAB4255zdqv3b4w1TuX9e
                             # amount=390000,
                             prev_hash=binascii.unhexlify('d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882'),
                             prev_index=0,
                             )

        out1 = proto_types.TxOutputType(address='1MJ2tj2ThBE62zXbBYA5ZaN3fdve5CPAz1',
                              amount=390000 - 10000,
                              script_type=proto_types.PAYTOADDRESS,
                              )

        out2 = proto_types.TxOutputType(op_return_data='test of the op_return data',
                              amount=0,
                              script_type=proto_types.PAYTOOPRETURN,
                              )

        with self.client:
            self.client.set_expected_responses([
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXMETA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=1, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.ButtonRequest(code=proto_types.ButtonRequest_SignTx),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.TxRequest(request_type=proto_types.TXFINISHED),
            ])
            (signatures, serialized_tx) = self.client.sign_tx('Bitcoin', [inp1, ], [out1, out2])

        self.assertEqual(binascii.hexlify(serialized_tx), '010000000182488650ef25a58fef6788bd71b8212038d7f2bbe4750bc7bcb44701e85ef6d5000000006a4730440220187b7b9c340a32fc8445418ad11fb3827d2e8bac7d730e1c9ad800353e7ba62f02206c0c5820ba8882c82923a39aee8d36d6d32e13daed73f7a3d6199de5f8e7ddfd0121023230848585885f63803a0a8aecdd6538792d5c539215c91698e315bf0253b43dffffffff0260cc0500000000001976a914de9b2a8da088824e8fe51debea566617d851537888ac00000000000000001c6a1a74657374206f6620746865206f705f72657475726e206461746100000000')

    def test_opreturn_big(self):
        self.setup_mnemonic_nopin_nopassphrase()

        # tx: d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882
        # input 0: 0.0039 BTC

        inp1 = proto_types.TxInputType(address_n=[0],  # 14LmW5k4ssUrtbAB4255zdqv3b4w1TuX9e
                             # amount=390000,
                             prev_hash=binascii.unhexlify('d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882'),
                             prev_index=0,
                             )

        out1 = proto_types.TxOutputType(address='1MJ2tj2ThBE62zXbBYA5ZaN3fdve5CPAz1',
                              amount=390000 - 10000,
                              script_type=proto_types.PAYTOADDRESS,
                              )

        out2 = proto_types.TxOutputType(op_return_data='FOXY' * 20,
                              amount=0,
                              script_type=proto_types.PAYTOOPRETURN,
                              )

        with self.client:
            self.client.set_expected_responses([
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXMETA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=1, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.ButtonRequest(code=proto_types.ButtonRequest_SignTx),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.TxRequest(request_type=proto_types.TXFINISHED),
            ])
            (signatures, serialized_tx) = self.client.sign_tx('Bitcoin', [inp1, ], [out1, out2])

        self.assertEqual(binascii.hexlify(serialized_tx), '010000000182488650ef25a58fef6788bd71b8212038d7f2bbe4750bc7bcb44701e85ef6d5000000006b483045022100a67a06774d3cdeda9201cec30a98994bf27dea55c2a684e9a2a7a3cf61b182d5022074671fa54005877d046dbc830dea43cdee666883fdb950470df65bea05a9978e0121023230848585885f63803a0a8aecdd6538792d5c539215c91698e315bf0253b43dffffffff0260cc0500000000001976a914de9b2a8da088824e8fe51debea566617d851537888ac0000000000000000536a4c50464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f5859464f585900000000')

    def test_opreturn_nonascii(self):
        self.setup_mnemonic_nopin_nopassphrase()

        # tx: d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882
        # input 0: 0.0039 BTC

        inp1 = proto_types.TxInputType(address_n=[0],  # 14LmW5k4ssUrtbAB4255zdqv3b4w1TuX9e
                             # amount=390000,
                             prev_hash=binascii.unhexlify('d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882'),
                             prev_index=0,
                             )

        out1 = proto_types.TxOutputType(address='1MJ2tj2ThBE62zXbBYA5ZaN3fdve5CPAz1',
                              amount=390000 - 10000,
                              script_type=proto_types.PAYTOADDRESS,
                              )

        out2 = proto_types.TxOutputType(op_return_data='\x00\x01\x02\x03\x04I Declare A Thumb War',
                              amount=0,
                              script_type=proto_types.PAYTOOPRETURN,
                              )

        with self.client:
            self.client.set_expected_responses([
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXMETA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=1, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.ButtonRequest(code=proto_types.ButtonRequest_SignTx),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1)),
                proto.TxRequest(request_type=proto_types.TXFINISHED),
            ])
            (signatures, serialized_tx) = self.client.sign_tx('Bitcoin', [inp1, ], [out1, out2])

        self.assertEqual(binascii.hexlify(serialized_tx), '010000000182488650ef25a58fef6788bd71b8212038d7f2bbe4750bc7bcb44701e85ef6d5000000006a47304402200814759f6406ca6106a110f1b453834164f729297ecf03602703c87d9fd2350102203c6917d586928a930ba7a7a9925453bc8bd195d8446348ba09e8f496300304a50121023230848585885f63803a0a8aecdd6538792d5c539215c91698e315bf0253b43dffffffff0260cc0500000000001976a914de9b2a8da088824e8fe51debea566617d851537888ac00000000000000001c6a1a000102030449204465636c6172652041205468756d622057617200000000')


    def test_nonzero_opreturn(self):
        self.setup_mnemonic_nopin_nopassphrase()

        # tx: d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882
        # input 0: 0.0039 BTC

        inp1 = proto_types.TxInputType(address_n=[0],  # 14LmW5k4ssUrtbAB4255zdqv3b4w1TuX9e
                             # amount=390000,
                             prev_hash=binascii.unhexlify('d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882'),
                             prev_index=0,
                             )

        out1 = proto_types.TxOutputType(address='1MJ2tj2ThBE62zXbBYA5ZaN3fdve5CPAz1',
                              amount=390000 - 10000 - 10000,
                              script_type=proto_types.PAYTOADDRESS,
                              )

        out1 = proto_types.TxOutputType(op_return_data='test of the op_return data',
                              amount=10000,
                              script_type=proto_types.PAYTOOPRETURN,
                              )

        with self.client:
            self.client.set_expected_responses([
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXMETA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=1, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify("d5f65ee80147b4bcc70b75e4bbf2d7382021b871bd8867ef8fa525ef50864882"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.Failure()
            ])
            self.assertRaises(CallException, self.client.sign_tx, 'Bitcoin', [inp1, ], [out1, ])

if __name__ == '__main__':
    unittest.main()
