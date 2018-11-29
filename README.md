# jdeppy
Python wrapper for [J.DepP](http://www.tkl.iis.u-tokyo.ac.jp/~ynaga/jdepp/), fast Japanese Dependency Parser.

# usage
```
from jdeppy import JDepP

jdepp = JDepp()
result = jdepp.parse('今日はいい天気ですね')
"""
result: list of Sentence
Sentence: s_id: int and blist: list of Bunsetsu
Bunsetsu: b_id: int and dep_id: int and mlist: list of Morph
  - b_id means 'Bunsetsu ID'
  - dep_id means 'Bunsetsu ID this Bunsetsu depends on'
Morph: surface: str and feature: list of str
  - feature's format is the same as mecab-python3
"""
```
