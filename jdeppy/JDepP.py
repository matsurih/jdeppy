import subprocess
from typing import Optional, Literal, List

from jdeppy.Sentence import Sentence
from jdeppy.Bunsetsu import Bunsetsu
from jdeppy.Morph import Morph

IPADIC = "ipadic"
UNIDIC = "unidic"
DicType = Literal[IPADIC, UNIDIC]


def create_morph_for_ipadic(jdepp_line: str) -> Morph:
    surf, args = tuple(jdepp_line.split("\t"))
    return Morph(surface=surf, feature=args.split(","))


def create_morph_for_unidic(jdepp_line: str) -> Morph:
    res = tuple(jdepp_line.split("\t"))
    return Morph(surface=res[0], feature=res[1:])


create_morph_fns = {
    IPADIC: create_morph_for_ipadic,
    UNIDIC: create_morph_for_unidic,
}


class JDepP:
    def __init__(self, option: Optional[str] = None, dic_type: DicType = IPADIC):
        self.devnul = open("/dev/null", "w")
        if option is None:
            self.option = []
        else:
            self.option = option.split(" ")
        if dic_type not in create_morph_fns:
            dic_type = IPADIC  # default
        self.dic_type = dic_type
        self.create_morph_fn = create_morph_fns[dic_type]

    def parse(self, sentence: Sentence) -> List[Sentence]:
        proc_mecab = subprocess.Popen(
            ["mecab"] + self.option,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=self.devnul,
        )
        proc_jdepp = subprocess.Popen(
            ["jdepp"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=self.devnul
        )
        mecab_stdout = proc_mecab.communicate((sentence + "\n").encode())
        mecab_result = mecab_stdout[0]
        jdepp_stdout = proc_jdepp.communicate(mecab_result)
        jdepp_lines = jdepp_stdout[0].decode().split("\n")
        jdepp_results = []
        sentence = None
        bunsetsu = None
        for jdepp_line in jdepp_lines:
            if jdepp_line.startswith("# S-ID:"):
                if sentence:
                    jdepp_results.append(sentence)
                sentence_id = int(
                    jdepp_line.split(";")[0].split(":")[1].replace(" ", "")
                )
                sentence = Sentence(s_id=sentence_id - 1, blist=[])
                continue

            elif jdepp_line.startswith("* "):
                if bunsetsu:
                    sentence.append_bunsetsu(bunsetsu)
                b_id, dep_id = tuple(
                    [int(c.replace("D", "")) for c in jdepp_line.split(" ") if c != "*"]
                )
                bunsetsu = Bunsetsu(b_id=b_id, dep_id=dep_id, mlist=[])
                continue

            elif jdepp_line == "EOS":
                sentence.append_bunsetsu(bunsetsu)
                jdepp_results.append(sentence)
                break

            else:
                morph = self.create_morph_fn(jdepp_line)
                bunsetsu.append_morph(morph)
                continue

        for s in jdepp_results:
            for b in s.blist:
                if b.dep_id == -1:
                    continue
                jdepp_results[s.s_id].blist[b.dep_id].append_child(b.b_id)

        return jdepp_results
