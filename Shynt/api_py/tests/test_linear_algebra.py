import unittest

import numpy as np


class TestJointCellVolume(unittest.TestCase):

    def test_matrix(self):
        # print("\n\n")
        
        a = np.array([
            [2,5],
            [3,1]
        ])

        b = np.array([
            [7,3],
            [1,4]
        ])
        c = np.array([
            [4,1],
            [3,10]
        ]) 

        vector = np.array([2,2])
        inv = np.linalg.inv(a)
        # print(a[0]*vector)
        # print("\n\n")
        assert 1 == 1



if __name__ == "__main__":
    unittest.main()