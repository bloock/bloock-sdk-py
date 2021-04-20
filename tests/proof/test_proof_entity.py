from unittest import TestCase, mock
from enchaintesdk.shared.utils import Utils
from enchaintesdk.proof.entity.proof_entity import Proof


class testProofEntity(TestCase):
    def test_is_valid_okay(self):
        leaves = [
            '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5']
        nodes = [
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
        ]
        bitmap = "bfdf7000"
        depth = "0004000600060005"
        self.assertTrue(Proof.isValid(Proof(leaves, nodes, depth, bitmap)),
                        'Proof should be valid.')

    def test_is_valid_minimalist(self):
        leaves = [
            '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5']
        nodes = []
        bitmap = "bf"
        depth = "0004"
        self.assertTrue(Proof.isValid(Proof(leaves, nodes, depth, bitmap)),
                        'Proof should be valid.')

    def test_is_valid_leaves_not_hex(self):
        leaves = [
            '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aeeg']
        nodes = [
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
        ]
        bitmap = "bfdf7000"
        depth = "000400060006000500030002000400060007000800090009"
        self.assertFalse(Proof.isValid(Proof(leaves, nodes, depth, bitmap)),
                         'Proof should be valid.')

    def test_is_valid_nodes_not_hex(self):
        leaves = [
            '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aeea']
        nodes = [
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeag",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
        ]
        bitmap = "bfdf7000"
        depth = "000400060006000500030002000400060007000800090009"
        self.assertFalse(Proof.isValid(Proof(leaves, nodes, depth, bitmap)),
                         'Proof should be valid.')

    def test_is_valid_bitmap_too_short(self):
        leaves = [
            '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5']
        nodes = [
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee",
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee",
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
        ]
        bitmap = "bf"
        depth = "0004000600060005000600060005000600060005"
        self.assertFalse(Proof.isValid(Proof(leaves, nodes, depth, bitmap)),
                         'Proof should be valid.')

    def test_is_valid_depth_too_short(self):
        leaves = [
            '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5']
        nodes = [
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
        ]
        bitmap = "bfdf7000"
        depth = "000400060006000"
        self.assertFalse(Proof.isValid(Proof(leaves, nodes, depth, bitmap)),
                         'Proof should be valid.')

    def test_is_valid_depth_too_long(self):
        leaves = [
            '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5']
        nodes = [
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
        ]
        bitmap = "bfdf7000"
        depth = "0004000600060"
        self.assertFalse(Proof.isValid(Proof(leaves, nodes, depth, bitmap)),
                         'Proof should be valid.')
