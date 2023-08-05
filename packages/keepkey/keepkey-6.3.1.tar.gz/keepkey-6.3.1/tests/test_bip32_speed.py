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
import time
from keepkeylib import tools

class TestBip32Speed(common.KeepKeyTest):

    def test_public_ckd(self):
        self.setup_mnemonic_nopin_nopassphrase()

        self.client.get_address('Bitcoin', [])  # to compute root node via BIP39

        for depth in range(8):
            start = time.time()
            self.client.get_address('Bitcoin', range(depth))
            delay = time.time() - start
            expected = (depth + 1) * 0.55
            print("DEPTH", depth, "EXPECTED DELAY", expected, "REAL DELAY", delay)
            self.assertLessEqual(delay, expected)

    def test_private_ckd(self):
        self.setup_mnemonic_nopin_nopassphrase()

        self.client.get_address('Bitcoin', [])  # to compute root node via BIP39

        for depth in range(8):
            start = time.time()
            self.client.get_address('Bitcoin', range(-depth, 0))
            delay = time.time() - start
            expected = (depth + 1) * 0.55
            print("DEPTH", depth, "EXPECTED DELAY", expected, "REAL DELAY", delay)
            self.assertLessEqual(delay, expected)

    def test_cache(self):
        self.setup_mnemonic_nopin_nopassphrase()

        start = time.time()
        for x in range(10):
            self.client.get_address('Bitcoin', [x, 2, 3, 4, 5, 6, 7, 8])
        nocache_time = time.time() - start

        start = time.time()
        for x in range(10):
            self.client.get_address('Bitcoin', [1, 2, 3, 4, 5, 6, 7, x])
        cache_time = time.time() - start

        print("NOCACHE TIME", nocache_time)
        print("CACHED TIME", cache_time)

        # Cached time expected to be at least 2x faster
        self.assertLessEqual(cache_time, nocache_time / 2.)
if __name__ == '__main__':
    unittest.main()
