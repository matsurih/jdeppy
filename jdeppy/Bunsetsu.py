from typing import List

from jdeppy.Morph import Morph


class Bunsetsu:
    def __init__(self, b_id: int, dep_id: int, mlist: List[Morph]):
        self.b_id = b_id
        self.dep_id = dep_id
        self.mlist = mlist
        self.children = []

    def append_morph(self, mrph: Morph):
        self.mlist.append(mrph)

    def append_child(self, child_id: int):
        self.children.append(child_id)
