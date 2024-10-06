from models.app import Model
from views.app import View
from controllers.app import Controller

def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()

if __name__ == "__main__":
    main()