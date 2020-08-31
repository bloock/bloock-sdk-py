import unittest
import numpy as np
from enchaintesdk.verifier import Verifier
from enchaintesdk.entity.hash import Hash


class TestVerifier(unittest.TestCase):
    """def test_verify_1_leaf(self):
        leaves = [np.array([0]*32, dtype='uint8')]
        nodes = []
        depths = np.array([0], dtype='uint8')
        bitmap = np.array([0], dtype='uint8')
        root = np.array([0]*32, dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_0(self):
        leaves = [np.array([0]*32, dtype='uint8')]
        nodes = [np.array([1]*32, dtype='uint8'),
                 np.array([55, 204, 95, 10, 183, 75, 225, 169, 26, 216, 79, 149, 29, 195, 120, 173, 46, 167,
                           91, 31, 187, 141, 101, 53, 137, 34, 143, 106, 45, 167, 226, 120], dtype='uint8')]
        depths = np.array([2, 2, 1], dtype='uint8')
        bitmap = np.array([96], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_1(self):
        leaves = [np.array([1]*32, dtype='uint8')]
        nodes = [np.array([0]*32, dtype='uint8'),
                 np.array([55, 204, 95, 10, 183, 75, 225, 169, 26, 216, 79, 149, 29, 195, 120, 173, 46, 167,
                           91, 31, 187, 141, 101, 53, 137, 34, 143, 106, 45, 167, 226, 120], dtype='uint8')]
        depths = np.array([2, 2, 1], dtype='uint8')
        bitmap = np.array([160], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_2(self):
        leaves = [np.array([2]*32, dtype='uint8')]
        nodes = [np.array([3, 127, 45, 161, 237, 218, 238, 67, 106, 133, 220, 204, 7, 34, 69, 228, 123, 196,
                           15, 21, 154, 156, 67, 94, 39, 81, 41, 150, 54, 177, 239, 3], dtype='uint8'),
                 np.array([3]*32, dtype='uint8')]

        depths = np.array([1, 2, 2], dtype='uint8')
        bitmap = np.array([160], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_3(self):
        leaves = [np.array([3]*32, dtype='uint8')]
        nodes = [np.array([3, 127, 45, 161, 237, 218, 238, 67, 106, 133, 220, 204, 7, 34, 69, 228, 123, 196,
                           15, 21, 154, 156, 67, 94, 39, 81, 41, 150, 54, 177, 239, 3], dtype='uint8'),
                 np.array([2]*32, dtype='uint8')]

        depths = np.array([1, 2, 2], dtype='uint8')
        bitmap = np.array([192], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_x0x0(self):
        leaves = [np.array([0]*32, dtype='uint8'),
                  np.array([2]*32, dtype='uint8')]
        nodes = [np.array([1]*32, dtype='uint8'),
                 np.array([3]*32, dtype='uint8')]
        depths = np.array([1, 1, 1, 1], dtype='uint8')
        bitmap = np.array([80], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_0x0x(self):
        leaves = [np.array([1]*32, dtype='uint8'),
                  np.array([3]*32, dtype='uint8')]
        nodes = [np.array([0]*32, dtype='uint8'),
                 np.array([2]*32, dtype='uint8')]
        depths = np.array([2, 2, 2, 2], dtype='uint8')
        bitmap = np.array([160], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_x00x(self):
        leaves = [np.array([0]*32, dtype='uint8'),
                  np.array([3]*32, dtype='uint8')]
        nodes = [np.array([1]*32, dtype='uint8'),
                 np.array([2]*32, dtype='uint8')]
        depths = np.array([2, 2, 2, 2], dtype='uint8')
        bitmap = np.array([96], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_0xx0(self):
        leaves = [np.array([1]*32, dtype='uint8'),
                  np.array([2]*32, dtype='uint8')]
        nodes = [np.array([0]*32, dtype='uint8'),
                 np.array([3]*32, dtype='uint8')]
        depths = np.array([2, 2, 2, 2], dtype='uint8')
        bitmap = np.array([144], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_00xx(self):
        leaves = [np.array([2]*32, dtype='uint8'),
                  np.array([3]*32, dtype='uint8')]
        nodes = [np.array([3, 127, 45, 161, 237, 218, 238, 67, 106, 133, 220, 204, 7, 34, 69, 228, 123, 196, 15,
                           21, 154, 156, 67, 94, 39, 81, 41, 150, 54, 177, 239, 3], dtype='uint8')]
        depths = np.array([1, 2, 2], dtype='uint8')
        bitmap = np.array([128], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))

    def test_verify_4_leaves_xx00(self):
        leaves = [np.array([0]*32, dtype='uint8'),
                  np.array([1]*32, dtype='uint8')]
        nodes = [np.array([55, 204, 95, 10, 183, 75, 225, 169, 26, 216, 79, 149, 29, 195, 120, 173, 46, 167, 91,
                           31, 187, 141, 101, 53, 137, 34, 143, 106, 45, 167, 226, 120], dtype='uint8')]
        depths = np.array([2, 2, 1], dtype='uint8')
        bitmap = np.array([32], dtype='uint8')
        root = np.array([236, 45, 107, 94, 128, 193, 173, 148, 130, 182, 250, 30, 47, 54, 61, 144,
                         13, 74, 126, 158, 114, 161, 132, 252, 253, 103, 236, 44, 168, 232, 117, 234], dtype='uint8')
        nroot = Verifier.verify(leaves, nodes, depths, bitmap)
        self.assertTrue(Hash.identicalKeys(root, nroot))"""
