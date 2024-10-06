from .base import ObservableModel
from .scorer import Scorer
from constants import docs as docsInput, feedback as fdInput

class SearchResult(ObservableModel):
    def __init__(self) -> None:
        super().__init__()

        self.docs = []

        self.scorer = Scorer(docsInput)
        self.scorer.learn_feedback(fdInput)

        print()

    
    def search(self, query):
        self.docs = [docsInput[self.scorer.score(query).argmax()]]