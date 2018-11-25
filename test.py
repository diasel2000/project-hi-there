import unittest

from Descriptor.miner import TextMiner
from Descriptor.descriptor import FoodDescriptor


class CalcTest(unittest.TestCase):
    def test_miner(self):
        image_text_miner = TextMiner()
        path_to_text_image = 'image.png'
        text_minig_result = image_text_miner.get_text(path_to_image=path_to_text_image)
        self.assertEqual(text_minig_result['status'], True)
        self.assertEqual(type(text_minig_result['result']), str)

    def test_descriptor(self):
        text = 'Tomorrow, and tomorrow, and tomorrow; creeps in this petty pace apple chiken pig '
        food_desc = FoodDescriptor()
        desc = food_desc.get_description(text=text)
        self.assertEqual(desc['fruits'], ['apple'])


if __name__ == '__main__':
    unittest.main()