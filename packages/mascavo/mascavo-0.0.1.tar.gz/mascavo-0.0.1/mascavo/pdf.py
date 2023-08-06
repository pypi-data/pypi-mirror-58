import io
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


def to_txt(infile: str, outfile: str):
    """
    Convert a pdf file to txt.
    :param infile: pdf file path;
    :param outfile: txt file path;
    :return: txt file path;
    """
    caching = True
    rsrcmgr = PDFResourceManager(caching=caching)
    codec = 'utf-8'
    pagenos = set()
    maxpages = 0
    password = ''
    laparams = LAParams()
    laparams.word_margin = float(0)
    laparams.line_margin = float(1)
    outfp = io.open(outfile, 'wt', encoding=codec, errors='ignore')
    device = TextConverter(rsrcmgr, outfp, laparams=laparams)
    fp = io.open(infile, 'rb')
    process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages,
                password=password, caching=caching, check_extractable=True)
    fp.close()
    device.close()
    outfp.close()
    return outfile
