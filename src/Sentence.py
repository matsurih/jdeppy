class Sentence:
    s_id = None
    blist = []

    def __init__(self, s_id, blist):
        self.s_id = s_id
        self.blist = blist

    def append_bunsetsu(self, bnst):
        self.blist.append(bnst)