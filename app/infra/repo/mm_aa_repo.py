from app.core.repo.aa_repo import AARepo

class MMAARepo(AARepo):
    def __init__(self):
        self.aa = "aa"
    def aa_method(self):
        return self.aa
