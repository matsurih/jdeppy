class Bunsetsu:
    b_id = None
    dep_id = None
    mlist = []

    def __init__(self, b_id, dep_id, mlist):
        self.b_id = b_id
        self.dep_id = dep_id
        self.mlist = mlist

    def append_morph(self, mrph):
        self.mlist.append(mrph)
