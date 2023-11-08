import unittest

from common.create_mails import _create_mails


class Create_mailsTest(unittest.TestCase):
    def setUp(self):
        # self.task = Task("Dummy task", False)
        pass

    def tearDown(self):
        # To be implemented if required
        pass

    def test_create_mails(self):
        self.assertEqual(
            _create_mails("green", "blue"), {"argA": "green", "argB": "blue"}
        )
