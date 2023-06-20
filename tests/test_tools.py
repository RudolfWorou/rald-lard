import unittest


class TestTools(unittest.TestCase):
    def test_integer_to_rald_lard_input(self):
        from raldlard.tools import integer_to_rald_lard_input
        self.assertEqual('O',integer_to_rald_lard_input(-8))
        self.assertEqual('O',integer_to_rald_lard_input(0))
        self.assertEqual('OCCC',integer_to_rald_lard_input(3))


    def test_outputs_to_integers(self):

        from raldlard.tools import outputs_to_integers
        
        self.assertEqual([0,2,1,None,1],outputs_to_integers(["O","OCC","OC","COC","CO"]))


if __name__=='__main__':
    unittest.main()