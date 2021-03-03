from typing import List

from jdeppy.Bunsetsu import Bunsetsu


class Sentence:
    def __init__(self, s_id: int, blist: List[Bunsetsu]):
        self.s_id = s_id
        self.blist = blist

    def append_bunsetsu(self, bnst: Bunsetsu):
        self.blist.append(bnst)
