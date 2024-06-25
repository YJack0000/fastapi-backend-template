from app.core.repo.aa_repo import AARepo

class ExampleLogic:
    def __init__(self, aa_repo: AARepo):
        self.aa_repo = aa_repo
    def example_method(self):
        return self.aa_repo.aa_method()
