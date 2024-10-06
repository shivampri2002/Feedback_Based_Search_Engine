from .root import Root
from .search import SearchView


class View:
    def __init__(self) -> None:
        self.root = Root()

        # self.frame_classes = {
        #     "search": SearchView,
        # }

        # self.current_view = None

        self.frames: Frames = {}  # type: ignore

        self._add_frame(SearchView, "search")


    # def switch(self, name):
    #     new_frame = self.frame_classes[name](self.root)
    #     if self.current_frame is not None:
    #         self.current_frame.destroy()
    #     self.current_frame = new_frame
    #     self.current_frame.grid(row=0, column=0, sticky="nsew")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()


    def start_mainloop(self):
        self.root.mainloop()