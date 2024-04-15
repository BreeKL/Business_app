from django.test import TestCase

# Create your tests here.
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls): # Run once to set up non-modified data for all class methods
        #print("setUpTestData: for test_forms.")
        pass

    def setUp(self): # Run once for every test method to set up clean data.
        #print("setUp: for test_forms.")
        pass

    def test_false_is_false(self): # test passes
        #print("Method: test_false_is_false for test_forms.")
        self.assertFalse(False)

    def test_false_is_true(self): # test fails
        #print("Method: test_false_is_true for test_forms.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self): #test passes
        #print("Method: test_one_plus_one_equals_two for test_forms.")
        self.assertEqual(1 + 1, 2)
