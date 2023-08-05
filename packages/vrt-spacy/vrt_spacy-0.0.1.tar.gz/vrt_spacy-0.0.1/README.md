# vrt_spacy

Python class for creating vrt-annotated corpora.
Still in very early testing stage.

Install by typing:
```bash
pip install vrt_spacy
```

Usage Example:
```python
from vrt import Corpus, S, Text
from vrt_spacy import Annotate
with Corpus("~","meinkorpus",4,"text_name") as c:
    annotate = Annotate(c, spacymodel="de_core_news_md")
    annotate("Das hier ist mein Text", text_name="Text1")
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