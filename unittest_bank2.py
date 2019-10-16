import unittest
from unittest.mock import MagicMock, patch, PropertyMock

from src.bank2 import Account, Card, SomeClass

class AccountTestCase(unittest.TestCase):

    def test_account_init(self):
        """"""
        ac = Account(123, "Jan",'Kowalski', 5000)
        ac2 = Account(456, "Zenon",'Kowalski',)
        self.assertEqual(ac.number, 123)
        self.assertEqual(ac.first_name, "Jan")
        self.assertEqual(ac.last_name, 'Kowalski')
        self.assertEqual(ac.owner, 'Jan Kowalski')

        self.assertEqual(ac.balance, 5000)
        self.assertEqual(ac2.balance, 0)

class CardTestCase(unittest.TestCase):
    def test_card_init(self):
        ac = Account(123, "Jan", 'Kowalski', 5000)
        card = Card(ac)
        self.assertEqual(card.get_account(), ac)
        self.assertEqual(len(card._pin), 5)

        with patch.object(
                Account,
                'owner',
                new_callable=PropertyMock) as owner_property:
            owner_property.return_value = 'Jan Kowalski'
            self.assertEqual(str(card), 'Jan Kowalski')


class MockTestCase(unittest.TestCase):

    @unittest.skip('not needed')
    def test_mock(self):
        a = SomeClass()
        print(a.hello())

        def foo():
            print("I am doing something else")

        mock_hello = MagicMock(
            return_value="hello world",
            side_effect=foo
        )

        a.hello = mock_hello
        print(a.hello())