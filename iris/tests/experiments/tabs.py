# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = "This is a test of a bunch of tabs"

    def run(self):
        # helper function
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()
        new_tab()

        # helper function
        navigate("https://www.google.com/?hl=EN")

        # core api function
        expected = exists("google_search.png", 10)
        assert_true(self, expected, 'google_search image found')
