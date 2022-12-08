import re

import Lex

class Error(Exception):
  pass

# ===================
# TOKEN VALUES
ID = 1
L_PAREN = 2
R_PAREN = 3
EQUALS = 4
STRING = 5
INT = 6
FLOAT = 7
MUL = 8
DIV = 9
MOD = 10
ADD = 11
SUB = 12
BOOL = 13
AND = 14
OR = 15
NOT = 16
  
# LANGUAGE CONSTRICTIONS IN REGEX
VAR_NAME = '^[A-Za-z]{0}[A-Za-z0-9_]{5,7}'
STRING_LIT = '(\'.*\')|(\".*\")'
INT_LIT = '[0-9]+'
FLOAT_LIT = '[0-9]+[\.]{1}[0-9]*'
BIN_OPERS = '\(\)\*/%\+-'
BOOL_OPERS = '((<|>)[=]?)|[&]{2}|[\|]{2}|[=]{2}|(![=]?)}'
BOOL = '(True|False)'


# ====================
# TOKEN CLASS DEFINED

class Token:  
  # INSTANCE VARIABLES
  symbol = ''
  token = 0

  def __init__(self, symbol):
    self.symbol = symbol
    self.token = self.getToken()

  # Tried to implement hashmap but for some reason my code wouldnt recognize it
  def getToken(self):
    try:
      int(self.symbol)
      return INT  
    except:
        try:
          float(self.symbol)
          return FLOAT
        except:
          pass
    if self.symbol == '(':
      return L_PAREN
    elif self.symbol == ')':
      return R_PAREN
    elif self.symbol == '*':
      return MUL
    elif self.symbol == '/':
      return DIV
    elif self.symbol == '%':
      return MOD
    elif self.symbol == '+':
      return ADD
    elif self.symbol == '-':
      return SUB
    elif self.symbol == '=':
      return EQUALS
    elif re.match(VAR_NAME, self.symbol):
      return ID
      
  def __repr__(self):
    return {self.token, self.symbol}

  def error(self, symbol):
    raise Error('Unable to parse value \'{}\' to token'.format(symbol))

  
# ====================
# LEXER CLASS DEFINED
  
class Lexer:
  # INSTANCE VARIABLES
  tokens = []
  current = 0
  currentToken = None

  # CONSTRUCTOR
  def __init__(self, text):
    self.tokens = self.toTokens(text)
    self.current = 0
    self.currentToken = self.tokens[self.current]

  def __repr__(self):
    return str(self.tokens)

  # METHOD TO GO TO NEXT TOKEN
  def getNextToken(self):
    if self.current < len(self.tokens):
      self.current += 1
      self.currentToken = self.tokens[self.current]

  # METHOD TO PARSE TEXT TO TOKENS
  def toTokens(self, text):
    tokens2 = []
    if re.match(VAR_NAME, text):
      tokens2.append({re.match(VAR_NAME, text).group(): ID})
      text = re.sub(VAR_NAME[1:] + '[\s]*', '', text)
      if re.match('^=', text):
        tokens2.append({re.match('^=', text).group(): EQUALS})
        text = re.sub('=' + '[\s]*', '', text)
    if re.match('^(\'.*\')|(\".*\")', text):
      tokens2.append({re.match('^(\'.*\')|(\".*\")'.group(), text): STRING})  
    elif re.match('\(\)\*/%\+-', text):
      operators = re.findall('\(\)\*/%\+-', text)
      print('Operators are:', operators)
      text = re.split('\(\)\*/%\+-', text)
      print(type(text))
    elif re.match(FLOAT_LIT, text):
      tokens2.append({float(re.match(FLOAT_LIT, text).group()): FLOAT})
    else:
      tokens2.append({int(text): INT})
    
      
            
      print('New2', text)
    print('New:', len(tokens2), tokens2)
    # if re.match('^[0-9]+(\.[0-9]*)', temp)
    tokens = []
    while self.current < len(self.tokens):
      self.getNextToken()
      tokens.append(currentToken)
    
    for x in text.split(' '):
      tokens.append(Token(x).getToken())
    return tokens

    # value = ''
    # for x in text:
    #   tokens.append(Token(eval(x)))
    
    # return tokens
    
  def error(self, value):
    raise Error('Unable to parse value \'{}\' to token'.format(value))
    
    # 
while True:
  text = input('Enter text:\n\t(Regex rule \"(end|exit)(\(\))?\" to break): ')
  if re.match('(end|exit)(\(\))?', text):
    break
  else:
    print(Lexer(text))
  

  
  # def __str__(self):
  #   return str(self.code)
  
  # def toCode(self, value):
  #   if type(value) == type('') and value.startswith('\"') and value.endswith('\"'):
  #     value = 'str_lit'
  #   elif type(value) == type(0):
  #     value = 'int_lit'
  #   elif type(value) == type(0.0):
  #     value = 'float_lit'
  #   elif type(value) == type(True):
  #     value = 'bool_lit'
  #   elif re.match('[A-Za-z]{1}[A-Za-z0-9_]{5,7}', value):
  #     value = 'id'
  #   if value in self.codes.keys():
  #     return self.codes[value]
  #   else:
  #     self.error(value)
      
