class Bunsetsu:
    def __init__(self, b_id, dep_id, mlist):
        self.b_id = b_id
        self.dep_id = dep_id
        self.mlist = mlist
        self.children = []

    def append_morph(self, mrph):
        self.mlist.append(mrph)

    def append_child(self, child_id):
        self.children.append(child_id)
