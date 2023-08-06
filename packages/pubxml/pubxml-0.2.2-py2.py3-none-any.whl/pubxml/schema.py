
import os, logging, re, sys, subprocess, tempfile
from bl.text import Text

log = logging.getLogger(__name__)

class Schema(Text):

    def __init__(self, fn, **args):
        """relaxng schema initialization.
        fn = the schema filename (required)
        """
        Text.__init__(self, fn=fn, **args)

    def trang(self, outfn=None, ext='.rng'):
        """use trang to convert the Schema to the given output filename or to the given extension
        SIDE EFFECT: creates a new file on the filesystem.
        """
        from . import JARS
        java = os.environ.get('java') or 'java'
        trang_jar = os.path.join(JARS, 'trang.jar')
        outfn = outfn or os.path.splitext(self.fn)[0] + ext
        stderr = tempfile.NamedTemporaryFile()
        try:
            result = subprocess.check_call(
                [java, "-jar", trang_jar, self.fn, outfn],
                universal_newlines=True,
                stderr=stderr)
        except subprocess.CalledProcessError as e:
            f = open(stderr.name, 'r+b')
            output = f.read(); f.close()
            raise RuntimeError(str(output, 'utf-8')).with_traceback(sys.exc_info()[2]) from None
        if result==0:
            return outfn
    
    def schematron(self, fn=None, outfn=None, ext='.sch'):
        """convert the Schema to schematron and save at the given output filename or with the given extension."""
        from .xslt import XSLT
        from . import PATH, XML, etree
        fn = fn or self.fn
        if os.path.splitext(fn)[-1].lower()==ext:
            return fn
        elif os.path.splitext(fn)[-1].lower()!='.rng':
            fn = Schema(fn=fn).trang(ext='.rng')
        rng2sch = XSLT(fn=os.path.join(PATH, 'xslts', 'rng2sch.xslt'))
        rng = XML(fn=fn)
        outfn = outfn or os.path.splitext(fn)[0]+ext
        sch = XML(fn=outfn, root=rng2sch.saxon9(rng.root).getroot())
        sch.write()
        return sch.fn

    def xhtml(self, outfn=None, ext='.xhtml', css=None, **params):
        """convert the Schema to XHTML with the given output filename or with the given extension."""
        from markdown import markdown
        from copy import deepcopy
        from bl.file import File
        from .xslt import XSLT
        from .rng import RNG
        from . import XML, PATH, etree
        rncfn = os.path.splitext(self.fn)[0] + '.rnc'
        rngfn = os.path.splitext(self.fn)[0] + '.rng'
        htmlfn = os.path.splitext(self.fn)[0] + '.html'
        if self.fn==rncfn or os.path.exists(rncfn):
            rngfn = Schema(rncfn).trang(ext='.rng')
        assert os.path.exists(rngfn)

        # convert all <r:define> elements into a <a:definition> blocks containing a compact syntax alternative
        rng = RNG(fn=rngfn)
        for define in rng.xpath(rng.root, "//r:define"):
            log.debug("%s %r" % (rng.tag_name(define), define.attrib))
            tempdefine = deepcopy(define)
            tempgrammar = deepcopy(rng.root); tempgrammar.text = '\n'
            for ch in tempgrammar.getchildren(): rng.remove(ch)
            tempgrammar.insert(0, tempdefine)
            for adoc in rng.xpath(tempdefine, ".//a:documentation | .//a:definition"):
                rng.remove(adoc)
            with tempfile.TemporaryDirectory() as tempdir:
                x = XML(fn=os.path.join(tempdir, 'define.rng'), root=tempgrammar)
                x.write()
                newfn = Schema(x.fn).trang(ext='.rnc')
                txt = open(newfn, 'rb').read().decode('utf-8')
                if '\n\n' in txt:
                    txt = txt[txt.index('\n\n')+1:].strip()
            adef = etree.Element("{%(a)s}definition" % RNG.NS)
            adef.text = txt
            adef.tail = '\n\t\t'
            log.debug(adef.text)
            annotations = rng.xpath(define, "a:*")
            if len(annotations) > 0:
                index = define.index(annotations[-1])+1
            else:
                index = 0
            define.insert(index, adef)
        rng.write()

        xslt = XSLT(fn=os.path.join(PATH, 'xslts', 'rng2md.xslt'))
        md = xslt.saxon9(rng.root, **params).strip()
        html_body = markdown(md, 
            output_format="xhtml5", 
            extensions=[                            # see https://python-markdown.github.io/extensions/
                'markdown.extensions.extra',    
                'markdown.extensions.admonition', 
                'markdown.extensions.headerid', 
                'markdown.extensions.sane_lists', 
                'markdown.extensions.toc']).strip()
        html_text = """<html><head><meta charset="UTF-8"/><style type="text/css">
            body {font-family:sans-serif;line-height:1.3;}
            h1,h2,h3 {margin:1em 0 .25em 0;}
            h1 {font-size:2rem;font-weight:normal;}
            h2 {font-size:1.2rem;font-weight:bold;}
            h3 {font-size:1.15rem;font-weight:normal;font-style:italic;}
            p {margin:0 0 .5rem 0;}
            p.subtitle {font-size:1.2rem;font-family:sans-serif;margin-bottom:1em;}
            code, p.code {font-family:monospace;font-size:0.9rem;color:#666;line-height:1.1;}
            pre {font-family:monospace;font-size:0.9rem;color:#666;line-height:1.1;margin-left:1.5rem;}
            hr {border:0;border-top:1px solid #999;margin:1rem 0;}
            </style></head><body>\n""" + html_body + """\n</body></html>"""
        html = XML(fn=htmlfn, root=html_text)
        return html

    @classmethod
    def from_tag(cls, tag, schemas, ext='.rnc'):
        """load a schema using an element's tag. schemas can be a string or a list of strings"""
        return cls(fn=cls.filename(tag, schemas, ext=ext))

    @classmethod
    def filename(cls, tag, schemas, ext='.rnc'):
        """given a tag and a list of schemas, return the filename of the schema.
        If schemas is a string, treat it as a comma-separated list.
        """
        if type(schemas)==str: 
            schemas = re.split("\s*,\s*", schemas)
        for schema in schemas:
            fn = os.path.join(schema, cls.dirname(tag), cls.basename(tag, ext=ext))
            if os.path.exists(fn):
                return fn

    @classmethod
    def dirname(cls, namespace):
        """convert a namespace url to a directory name. 
            Also accepts an Element 'tag' with namespace prepended in {braces}."""
        md = re.match("^\{?(?:[^:]+:/{0,2})?([^\}]+)\}?", namespace)
        if md is not None:
            dirname = re.sub("[/:]", '_', md.group(1))
        else:
            dirname = ''
        return dirname

    @classmethod
    def basename(cls, tag, ext='.rnc'):
        return re.sub("\{[^\}]*\}", "", tag) + ext
