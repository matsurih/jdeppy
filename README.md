# jdeppy

Python wrapper for [J.DepP](http://www.tkl.iis.u-tokyo.ac.jp/~ynaga/jdepp/), fast Japanese Dependency Parser.

# Requisites

You need to install J.DepP. 

See "Download & Setup" section in http://www.tkl.iis.u-tokyo.ac.jp/~ynaga/jdepp/ 

# Install

```
pip install jdeppy
```

# Usage

```python
from jdeppy.JDepP import JDepP

jdepp = JDepP()
result = jdepp.parse('今日はいい天気ですね')

# result: list of Sentences
# Sentence: s_id: int and blist: list of Bunsetsus
# Bunsetsu: b_id: int and dep_id: int and mlist: list of Morphs
#   - b_id means 'Bunsetsu ID'
#   - dep_id means 'Bunsetsu ID this Bunsetsu depends on'
# Morph: surface: str and feature: list of strs
#   - feature's format is the same as mecab-python3

```

# License
This software is released under the MIT License, see LICENSE.txt.
