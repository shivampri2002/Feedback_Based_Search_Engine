class ObservableModel:
    def __init__(self) -> None:
        self._event_listeners : dict = {}

    def add_event_listener(self, event, fn):
        try:
            self._event_listeners[event].append(fn)
        except KeyError:
            self._event_listeners[event] = [fn]

    def trigger_event(self, event):
        if event not in self._event_listeners.keys():
            return
        for func in self._event_listeners[event]:
            func(self)


