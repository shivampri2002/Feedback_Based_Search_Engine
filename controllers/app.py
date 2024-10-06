from .search import SearchController
from models.app import Model
from views.app import View

class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.search_controller = SearchController(self.model, self.view)

        

    def start(self):
        self.view.switch("search")

        self.view.start_mainloop()