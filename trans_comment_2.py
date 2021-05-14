import sys
import re
from googletrans import Translator

translator = Translator()


def remove_emoji(string):
  emoji_pattern = re.compile("["
                             u"\U0001F600-\U0001F64F"  # emoticons
                             u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                             u"\U0001F680-\U0001F6FF"  # transport & map symbols
                             u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                             u"\U00002702-\U000027B0"
                             u"\U000024C2-\U0001F251"
                             "]+", flags=re.UNICODE)
  return emoji_pattern.sub(r'', string)


#my_file = codecs.open( 'data_translate.csv' , 'r' , 'utf-8' , errors='strict')

for row in sys.stdin:
  #line = str(line).strip().split('|')
  incident, nav_verbatim = str(row).strip().split('|')
  nav_verbatim = remove_emoji(nav_verbatim)

  try:
    trans_txt = translator.translate(nav_verbatim.replace('.', ';'), dest='en').text
    op_txt = incident + '|' + nav_verbatim + '|' + trans_txt
    print(op_txt.strip())
  except:
    op_txt = incident + '|' + nav_verbatim + '|' + 'no_translation'
    print(op_txt.strip())
