import subprocess
from jdeppy.Sentence import Sentence
from jdeppy.Bunsetsu import Bunsetsu
from jdeppy.Morph import Morph


class JDepP:
    def __init__(self, option=None):
        self.devnul = open('/dev/null', 'w')
        if option is None:
            self.option = []
        else:
            self.option = option.split(' ')

    def parse(self, sentence):
        proc_mecab = subprocess.Popen(['mecab'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=self.devnul)
        proc_jdepp = subprocess.Popen(['jdepp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=self.devnul)
        mecab_stdout = proc_mecab.communicate((sentence + '\n').encode())
        mecab_result = mecab_stdout[0]
        jdepp_stdout = proc_jdepp.communicate(mecab_result)
        jdepp_lines = jdepp_stdout[0].decode().split('\n')
        jdepp_results = []
        sentence = None
        bunsetsu = None
        for jdepp_line in jdepp_lines:
            if jdepp_line.startswith('# S-ID:'):
                if sentence:
                    jdepp_results.append(sentence)
                sentence_id = int(jdepp_line.split(';')[0].split(':')[1].replace(' ', ''))
                sentence = Sentence(s_id=sentence_id, blist=[])
                continue

            elif jdepp_line.startswith('*'):
                if bunsetsu:
                    sentence.append_bunsetsu(bunsetsu)
                b_id, dep_id = tuple([int(c.replace('D', '')) for c in jdepp_line.split(' ') if c != '*'])
                bunsetsu = Bunsetsu(b_id=b_id, dep_id=dep_id, mlist=[])
                continue

            elif jdepp_line == 'EOS':
                sentence.append_bunsetsu(bunsetsu)
                jdepp_results.append(sentence)
                break

            else:
                surf, args = tuple(jdepp_line.split('\t'))
                morph = Morph(surface=surf, feature=args.split(','))
                bunsetsu.append_morph(morph)
                continue

        return jdepp_results
