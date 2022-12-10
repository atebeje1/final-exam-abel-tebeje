import re
from Token import token

class LexicalError(Exception):
  pass
  
class lexer:
  def __init__(self, text:str):
    self.text = text
    self.tokens = self.toTokens()
  def error(self, details = None):
    raise LexicalError(details)
  
  def toTokens(self):
    result = []
    isMultiLineComment = False
    for line in self.text.split('\n'):
      original = line
      id = '[A-Za-z]{1}[A-Za-z0-9_]{5,7}'
      if line == '':
        continue
      if isMultiLineComment:
        if re.search('\*/', line):
          line = re.sub('^.*\*/','<E_MLC>', line)
          isMultiLineComment = False
        else:
          line = '<MLC>'
          continue
      elif re.search('//', line):
        line = re.sub('//.*$', '<SLC>', line)
      elif re.search('/*', line):
        isMultiLineComment = True
        line = re.sub('/\*', '<S_MLC>', line)
      if re.search(id, line):
        line = re.sub(id,'<V_ID>', line)
        if re.search('=', line) and not re.search('==', line):
          line = re.sub('=', '<A_OP>', line)
        if re.search('\".*\"', line):
          line = re.sub('\".*\"', '<STR>', line)
      char_pattern = '\'\\?.\''
      print(re.search('\'[A-Za-z0-9_]\'', line))
      print(re.search('\'(\\?\D)?\'', line))
      if re.search('\'.\'', line):
        line = re.sub('\'.\'', '<CHAR>', line)
      if re.search('[0-9]+\.[0-9]*[Nn]?', line):
        line = re.sub('[0-9]+\.[0-9]*', '<REAL>', line)
      if re.search('[0-9]+[Nn]?', line):
        line = re.sub('[0-9]+[Nn]?', '<NATNUM>', line)
      if re.search('true|false', line):
        line = re.sub('true|false', '<BOOL>', line)
      if re.search('function', line):
        print(True)
        line = re.sub('function', '<FUNCT>', line)
        if re.search(id, line):
          print('RESULT:', re.search(id, line))
        for var in re.findall(id, line):
          if var != 'FUNCTION':
            line = re.sub(var, '<FNAME>', line) 
            line = re.sub('\(', '<BARGS>', line)
            while re.match('id', line):
              line = re.sub(id, '<A_ID>', line)
              if ',' in line:
                line = re.sub(',', '<SPRTR>', line)
            line = re.sub('\)','<EARGS>', line)
            line = re.sub(':', '<B_BLK>', line)
      elif line.startswith('end'):
        line = re.sub('end', '<E_BLK>', line)
      line = re.sub('><', '> <', line)
      print('\tOriginal line: {}'.format(original))
      print('\t\tAdjusted line: {}'.format(line))
      for lexeme in line.split(' '):
        if lexeme == '<MLC>':
          continue
        result.append(token(lexeme))
      result.append(token('<EOL>'))
      print('\t\t\t{}'.format(result))