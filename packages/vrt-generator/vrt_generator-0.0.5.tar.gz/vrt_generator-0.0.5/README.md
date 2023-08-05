# vrt_generator
Python class for creating vrt-annotated corpora.
Still in very early testing stage.

Install by typing:
```bash
pip install git+https://github.com/miweru/vrt_generator
```

Usage Example:
```python
from vrt import Corpus, P, S, Text, annotext_spacy
with Corpus("~","meinkorpus",4,"text_name") as c:
    c.add_spacy()
    annotext_spacy(c, "Das hier ist mein Text", text_name="Text1")
    with Text(c, text_name="Text2") as t:
        with S(c) as s:
            s.writep("Test","TAG","TAG","Lemma")  
```

Features:
-
- Represent Corpus, Text, P and S Attributes
- Integration of spacy for automatic generation of a vrt-representation of texts
- Using Context Manager for xml-hierarchy representation
- Reduces to utf8mb3 and checks formatting compatibility