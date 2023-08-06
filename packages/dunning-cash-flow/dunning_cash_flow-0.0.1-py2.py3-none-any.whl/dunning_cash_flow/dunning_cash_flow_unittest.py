# -*- coding: utf-8 -*-

# Copyright (c) ALT-F1 SPRL, Abdelkrim Boujraf. All rights reserved.
# Licensed under the EUPL License, Version 1.2. See LICENSE in the project root for license information.

import dunning_cash_flow as dcf
import os
import pandas as pd
import unittest


class DunningCashFlowTests(unittest.TestCase):

    """ class for running unittests """

    def setUp(self):
        """ Your setUp """
        self.Auth = dcf.Authentication()
        # {"code":"err_not_authorised","message":"Not authorised"}


    def test_login_failed(self):
        """ Test that the authorization code is {'message': 'Not logged in'}"""
        error_code = {'code': 'err_not_authorised', 'message': 'Not authorised'}
        self.Auth.login(api_token="A_WRONG_CODE")
        self.assertEqual(self.Auth.authorization, error_code)

    def test_login_successfull(self):
        """ Test that the authorization code is fulfilled"""

        self.Auth.login(api_token=os.environ['twikeyApiToken'])
        self.assertIsNotNone(self.Auth.authorization)


suite = unittest.TestLoader().loadTestsFromTestCase(DunningCashFlowTests)
unittest.TextTestRunner(verbosity=2).run(suite)
