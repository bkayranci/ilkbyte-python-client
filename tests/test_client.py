import unittest

from ilkbyte.client import Ilkbyte


class TestIlkbyteClient(unittest.TestCase):

    def setUp(self) -> None:
        # @TODO: mock api
        self._client = Ilkbyte()

    def test_account(self):
        self.assertDictEqual({}, self._client.get_account())


if __name__ == '__main__':
    unittest.main()
