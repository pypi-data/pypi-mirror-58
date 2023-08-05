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

from __future__ import print_function

import unittest
import common
import binascii
import hashlib
import struct

from keepkeylib.client import CallException
import keepkeylib.types_pb2 as proto_types

def check_path(identity):
    m = hashlib.sha256()
    m.update(struct.pack("<I", identity.index))
    uri = ''
    if identity.proto: uri += identity.proto + '://'
    if identity.user: uri += identity.user + '@'
    if identity.host: uri += identity.host
    if identity.port: uri += ':' + identity.port
    if identity.path: uri += identity.path
    m.update(uri)
    print('hash:', m.hexdigest())
    (a, b, c, d, _, _, _, _) = struct.unpack('<8I', m.digest())
    address_n = [0x80000000 | 13, 0x80000000 | a, 0x80000000 | b, 0x80000000 | c, 0x80000000 | d]
    print('path:', 'm/' + '/'.join([str(x) for x in address_n]))

class TestMsgSignidentity(common.KeepKeyTest):

    def test_sign(self):
        self.setup_mnemonic_nopin_nopassphrase()

        hidden = binascii.unhexlify('cd8552569d6e4509266ef137584d1e62c7579b5b8ed69bbafa4b864c6521e7c2')
        visual = '2015-03-23 17:39:22'

        # URI  : https://satoshi@bitcoin.org/login
        # hash : d0e2389d4c8394a9f3e32de01104bf6e8db2d9e2bb0905d60fffa5a18fd696db
        # path : m/2147483661/2637750992/2845082444/3761103859/4005495825
        identity = proto_types.IdentityType(proto='https', user='satoshi', host='bitcoin.org', port='', path='/login', index=0)
        sig = self.client.sign_identity(identity, hidden, visual)
        self.assertEqual(sig.address, '17F17smBTX9VTZA9Mj8LM5QGYNZnmziCjL')
        self.assertEqual(binascii.hexlify(sig.public_key), '023a472219ad3327b07c18273717bb3a40b39b743756bf287fbd5fa9d263237f45')
        self.assertEqual(binascii.hexlify(sig.signature), '20f2d1a42d08c3a362be49275c3ffeeaa415fc040971985548b9f910812237bb41770bf2c8d488428799fbb7e52c11f1a3404011375e4080e077e0e42ab7a5ba02')

        # URI  : ftp://satoshi@bitcoin.org:2323/pub
        # hash : 79a6b53831c6ff224fb283587adc4ebae8fb0d734734a46c876838f52dff53f3
        # path : m/2147483661/3098912377/2734671409/3632509519/3125730426
        identity = proto_types.IdentityType(proto='ftp', user='satoshi', host='bitcoin.org', port='2323', path='/pub', index=3)
        sig = self.client.sign_identity(identity, hidden, visual)
        self.assertEqual(sig.address, '1KAr6r5qF2kADL8bAaRQBjGKYEGxn9WrbS')
        self.assertEqual(binascii.hexlify(sig.public_key), '0266cf12d2ba381c5fd797da0d64f59c07a6f1b034ad276cca6bf2729e92b20d9c')
        self.assertEqual(binascii.hexlify(sig.signature), '20bbd12dc657d534fc0f7e40186e22c447e0866a016f654f380adffa9a84e9faf412a1bb0ae908296537838cf91145e77da08681c63d07b7dca40728b9e6cb17cf')

        # URI  : ssh://satoshi@bitcoin.org
        # hash : 5fa612f558a1a3b1fb7f010b2ea0a25cb02520a0ffa202ce74a92fc6145da5f3
        # path : m/2147483661/4111640159/2980290904/2332131323/3701645358
        identity = proto_types.IdentityType(proto='ssh', user='satoshi', host='bitcoin.org', port='', path='', index=47)
        sig = self.client.sign_identity(identity, hidden, visual, ecdsa_curve_name='nist256p1')
        self.assertEqual(sig.address, '')
        self.assertEqual(binascii.hexlify(sig.public_key), '0373f21a3da3d0e96fc2189f81dd826658c3d76b2d55bd1da349bc6c3573b13ae4')
        self.assertEqual(binascii.hexlify(sig.signature), '005122cebabb852cdd32103b602662afa88e54c0c0c1b38d7099c64dcd49efe908288114e66ed2d8c82f23a70b769a4db723173ec53840c08aafb840d3f09a18d3')

        # URI  : ssh://satoshi@bitcoin.org
        # hash : 5fa612f558a1a3b1fb7f010b2ea0a25cb02520a0ffa202ce74a92fc6145da5f3
        # path : m/2147483661/4111640159/2980290904/2332131323/3701645358
        identity = proto_types.IdentityType(proto='ssh', user='satoshi', host='bitcoin.org', port='', path='', index=47)
        sig = self.client.sign_identity(identity, hidden, visual, ecdsa_curve_name='ed25519')
        self.assertEqual(sig.address, '')
        self.assertEqual(binascii.hexlify(sig.public_key), '000fac2a491e0f5b871dc48288a4cae551bac5cb0ed19df0764d6e721ec5fade18')
        self.assertEqual(binascii.hexlify(sig.signature), '00f05e5085e666429de397c70a081932654369619c0bd2a6579ea6c1ef2af112ef79998d6c862a16b932d44b1ac1b83c8cbcd0fbda228274fde9e0d0ca6e9cb709')

        # Verify that format characters in user supplied strings do not cause UB
        identity = proto_types.IdentityType(proto='ssh', user='%n%s%x%p', host='%n%s%x%p', port='', path='', index=47)
        sig = self.client.sign_identity(identity, hidden, visual, ecdsa_curve_name='ed25519')
        self.assertEqual(sig.address, '')
        self.assertEqual(binascii.hexlify(sig.public_key), '00f3ae8a64f2aa19baf8f7a8b2e48e8ea232d8dd368df322c4bd25ce8d4637b399')
        self.assertEqual(binascii.hexlify(sig.signature), '00fa861cca76ed06f53174c84f8de1881f7f467c424c9c03e41be345cf9ad3f38f19ea01e32d37e2ccf3d9f104c617e99e4d2062397894c32158686d0222a9490b') 

    def test_vuln1974(self):
        self.setup_mnemonic_nopin_nopassphrase()

        hidden = binascii.unhexlify('cd8552569d6e4509266ef137584d1e62c7579b5b8ed69bbafa4b864c6521e7c2')
        visual = '2015-03-23 17:39:22'

        # Check that firmware doesn't crash when we don't provide a visual challenge
        identity = proto_types.IdentityType(proto='ssh', user='satoshi', host='bitcoin.org', port='', path='', index=47)
        sig = self.client.sign_identity(identity, hidden, None, ecdsa_curve_name='ed25519')
        self.assertEqual(sig.address, '')
        self.assertEqual(binascii.hexlify(sig.public_key), '000fac2a491e0f5b871dc48288a4cae551bac5cb0ed19df0764d6e721ec5fade18')
        self.assertEqual(binascii.hexlify(sig.signature), '00f05e5085e666429de397c70a081932654369619c0bd2a6579ea6c1ef2af112ef79998d6c862a16b932d44b1ac1b83c8cbcd0fbda228274fde9e0d0ca6e9cb709')

        # Check that firmware doesn't crash when we don't provide a hidden challenge
        identity = proto_types.IdentityType(proto='ssh', user='satoshi', host='bitcoin.org', port='', path='', index=47)
        sig = self.client.sign_identity(identity, None, visual, ecdsa_curve_name='ed25519')
        self.assertEqual(sig.address, '')
        self.assertEqual(binascii.hexlify(sig.public_key), '000fac2a491e0f5b871dc48288a4cae551bac5cb0ed19df0764d6e721ec5fade18')
        self.assertEqual(binascii.hexlify(sig.signature), '009d24b56cded5a7d9c517c9fdd43601feecd69c298bc71361f840ca041ab6ee98bfc0c386dc1bfc1b342894dc702e9b19ea3b0665a1801c82b6a814149568ad09')

        # Check that firmware doesn't crash when we don't provide a hidden challenge
        identity = proto_types.IdentityType(proto='ssh', user='satoshi', host='bitcoin.org', port='', path='', index=47)
        sig = self.client.sign_identity(identity, None, None, ecdsa_curve_name='ed25519')
        self.assertEqual(sig.address, '')
        self.assertEqual(binascii.hexlify(sig.public_key), '000fac2a491e0f5b871dc48288a4cae551bac5cb0ed19df0764d6e721ec5fade18')
        self.assertEqual(binascii.hexlify(sig.signature), '009d24b56cded5a7d9c517c9fdd43601feecd69c298bc71361f840ca041ab6ee98bfc0c386dc1bfc1b342894dc702e9b19ea3b0665a1801c82b6a814149568ad09')


if __name__ == '__main__':
    unittest.main()
