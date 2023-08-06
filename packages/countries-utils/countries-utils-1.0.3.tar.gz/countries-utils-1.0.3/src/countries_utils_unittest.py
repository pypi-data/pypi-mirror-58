# -*- coding: utf-8 -*-

# Copyright (c) ALT-F1 SPRL, Abdelkrim Boujraf. All rights reserved.
# Licensed under the EUPL License, Version 1.2. See LICENSE in the project root for license information.

import countries_utils as cu
import os
import pandas as pd
import unittest

class CountriesUtilsTests(unittest.TestCase):

    """ class for running unittests """

    def setUp(self):
        """ Your setUp """
        TEST_INPUT_DIR = 'data/'
        test_file_name = 'places.csv'

        try:

            data = pd.read_csv(
                os.path.join(os.getcwd(), TEST_INPUT_DIR, test_file_name),
                sep=',',
                header=0
            )
        except IOError:
            print("cannot open file")
        self.fixture = data
        
        self.expected_country_iso_list = [
            'Belgium',
            'Belgium',
            'Belgium',
            'Netherlands',
            'Netherlands',
            'France',
            'France'
        ]

        self.expected_country_iso_set = {
            'Belgium',
            'France',
            'Netherlands'
        }

        self.country_iso_list, self.country_iso_set  = cu.get_list_of_countries_in_text(
            self.fixture,
            place="place",
            languages_to_check=["en", "fr", "nl"]
        )

    def test_country_iso_list(self):
        """ Test that the country_iso_list is equal to what is expected"""

        self.assertEqual(self.country_iso_list, self.expected_country_iso_list)

    def test_country_iso_set(self):
        """ Test that the country_iso_set is equal to what is expected"""

        self.assertEqual(self.country_iso_set, self.expected_country_iso_set)


suite = unittest.TestLoader().loadTestsFromTestCase(CountriesUtilsTests)
unittest.TextTestRunner(verbosity=2).run(suite)
