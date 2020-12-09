import unittest

from ilkbyte.client import Ilkbyte
from ilkbyte.exception import ConfigurationError


class TestIlkbyteClient(unittest.TestCase):

    # def setUp(self) -> None:
    #     # @TODO: mock api
    #     self._client = Ilkbyte()

    def test_get_instance(self):
        with self.assertRaises(ConfigurationError):
            self._client = Ilkbyte()


if __name__ == '__main__':
    unittest.main()
