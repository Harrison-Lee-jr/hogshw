from test_self_frame210109.app import App


class TestSearch:
    def setup(self):
        self.app=App()
    def test_search(self):
        self.app.start().start().goto_main().goto_market().goto_search().search()