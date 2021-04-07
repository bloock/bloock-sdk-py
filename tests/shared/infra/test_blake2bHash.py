'''import unittest
import numpy as np
from enchaintesdk.shared.infra.blake2bHash import Blake2bHash

class TestBlake2bHash(unittest.TestCase):
    def test_hash(self):
        data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='uint8')
        self.assertEqual(Blake2bHash.hash(data),
                        'e283ce217acedb1b0f71fc5ebff647a1a17a2492a6d2f34fb76b994a23ca8931')'''
