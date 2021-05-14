from googletrans import Translator
import sys
import unicodedata

translator = Translator()


def make_translation(txt):
    return translator.translate(txt, dest='en').text


cnt = 0

for row in sys.stdin:

    cnt = cnt + 1

    line = str(row).strip().split('|')

    incident, nav_verbatim = line[20], line[21]

    try:
        trans_txt = make_translation(nav_verbatim)
    except:
        trans_txt = 'unicode_issue'

    op_txt = incident + '|' + nav_verbatim + '|' + trans_txt
    print(op_txt)
