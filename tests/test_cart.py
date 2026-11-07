import unittest
from aims.cart import Cart


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        for _ in range(20):
            cart.add_dvd(object())

        # DVD thứ 21 phải không được thêm
        self.assertFalse(cart.add_dvd(object()))


if __name__ == "__main__":
    unittest.main()