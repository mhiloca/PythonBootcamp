import unittest
from activities import eat, nap, is_funny, laugh


class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """should have a positive message"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a temple"
        )

    def test_eat_unhealthy(self):
        """shouel have  give up message"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO"
        )

    def test_is_healthy_boolean(self):
        """is_healthy must be a bollean"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
        """should have a message saying how you feel"""
        self.assertEqual(
            nap(1), "I'm feeling refreshed after 1 hour nap!"
        )

    def test_long_nap(self):
        """should have a message saying how you feel"""
        self.assertEqual(
            nap(3), "Urgh, I overslept, I din't mean to sleep for 3 hours"
        )

    def test_is_funny_tim(self):
        """tim should not be funny"""
        # self.assertFalse(is_funny("tim"), "should not be funny")
        self.assertEqual(is_funny("tim"), False)

    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'hahaha', 'tehehe'))


if __name__ == "__main__":
    unittest.main()
