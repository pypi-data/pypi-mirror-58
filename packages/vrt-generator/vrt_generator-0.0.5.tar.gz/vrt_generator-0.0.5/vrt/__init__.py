from smart_open import open
from os import path
import csv
from pathlib import Path
from xml.sax.saxutils import escape

ALLOWED_LETTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"


def check_letters(text):
    return min({l in ALLOWED_LETTERS for l in text}) if text else True


def to_utf8mb3(t):
    return "".join([c if ord(c) < 2 ** 16 else "_e" for c in t])


class Corpus:
    def writeline(self, line):
        assert "\n" not in line
        self._fo.write(line + "\n")

    def writemeta(self, metadata):
        self._meta.writerow(metadata)

    def __init__(self, target_folder, name, pattrs, *args):
        target_folder = path.expanduser(target_folder)
        target_folder = Path(target_folder)
        assert path.isdir(target_folder)
        try:
            assert check_letters(name)
        except Exception as e:
            print("Wrong param is:'{}".format(name))
            raise e

        assert isinstance(pattrs, int)
        assert pattrs > 0
        self._pattrs = pattrs

        self.fieldnames = ["id"]
        for arg in args:
            assert check_letters(arg)
            self.fieldnames.append(arg)

        self._fo = open(
            path.join(target_folder, name + ".vrt.gz"),
            "w",
            encoding="utf8"
        )

        self._metaf = open(
            path.join(target_folder, name + ".meta.tsv"),
            "w",
            encoding="utf8",
            newline=""
        )

        self._meta = csv.DictWriter(self._metaf,
                                    fieldnames=self.fieldnames,
                                    delimiter="\t",
                                    lineterminator="\n"
                                    )

        self.writeline("<corpus>")

        self._idcount = -1

    def close(self):
        self.writeline("</corpus>")
        self._fo.close()
        self._metaf.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def getid(self):
        self._idcount += 1
        return "t{}".format(self._idcount)


class Sattribute:
    ATTRNAME = None

    def __init__(self, corpus, attrib_name):
        assert isinstance(corpus, Corpus)
        assert not corpus._fo.closed
        self.writeline = corpus.writeline
        self._pattrs = corpus._pattrs

    def writep(self, *args):
        assert len(args) == self._pattrs
        args = [to_utf8mb3(escape(line)) for line in args]
        self.writeline("\t".join(args))

    def close(self):
        self.writeline("</{}>".format(self.ATTRNAME))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


class Text(Sattribute):
    ATTRNAME = "text"

    def __init__(self, corpus, **kwargs):
        super().__init__(corpus, self.ATTRNAME)
        assert "id" not in kwargs

        ident = corpus.getid()
        for argn, arg in kwargs.items():
            assert argn in corpus.fieldnames
            try:
                assert check_letters(arg)
            except Exception as e:
                print("Exception was thrown when checking '{}".format(arg))
                raise e
        self.writeline('<text id="{}">'.format(ident))
        kwargs["id"] = ident
        corpus.writemeta(kwargs)


class P(Sattribute):
    """
    This Class has no Metadata
    """
    ATTRNAME = "p"

    def __init__(self, corpus):
        super().__init__(corpus, self.ATTRNAME)
        self.writeline('<{}>'.format(self.ATTRNAME))


class S(Sattribute):
    """
    This Class has no Metadata
    """
    ATTRNAME = "s"

    def __init__(self, corpus):
        super().__init__(corpus, self.ATTRNAME)
        self.writeline('<{}>'.format(self.ATTRNAME))



"""
def _testcode():
    with Corpus("~", "mycorpus", 4, "textname", "author") as c:
        with Text(c, textname="Demotext2", author="Frank_N") as text:
            with P(c) as paragraph:
                with S(c) as s:
                    s.writep("Das", "PDS", "PRON", "der")
                    s.writep("hier","ADV","ADV","hier")
"""
