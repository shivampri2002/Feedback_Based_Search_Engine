class SearchController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["search"]
        self._bind()

    def _bind(self):
        self.frame.search_btn.config(command=self.on_search)

    def on_search(self):
        search_query = self.frame.search_entry.get()
        self.model.auth.logout()