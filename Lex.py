class Error(Exception):
  pass
class RDA:
  tokens = []
  current = 0
  currentToken = None
  def __init__(self, tokens:list) -> None:
    self.tokens = tokens
    self.current = 0
    self.currentToken = tokens[self.current]
    self.generate()

  def __str__(self):
    return ' '.join([str(item) for item in self.tokens])

  def getNextToken(self):
    if self.current < len(self.tokens):
      self.current += 1

    self.currentToken = self.tokens[self.current]

  def bool_expr(self):
    pass
  def band(self):
    pass
  def beq(self):
    pass
  def brel(self):
    pass
  def bexpr(self):
    pass
  def bterm(self):
    # <term> --> <factor> { (`*` | `/` | '%') <factor> }
    self.factor()
    while self.current() in ('*', '/', '%'):
      self.getNextToken()
      self.bfactor()
  def bnot(self):
    pass
  def bfactor(self):
    '''
    <bfactor> --> `id` | `int_lit` | `float_lit` | `bool_lit` | `(` <bexpr> `)`
    FIRST(<bfactor>) -> {id}{int_lit}{float_lit}{'('}
    '''
    if self.currentToken in ('id', 'int_lit', 'float_lit'):
      self.getNextToken()
    elif self.currentToken == '(':
      self.getNextToken()
      self.bexpr()
      if self.getCurrentToken == ')':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()


  
  def stmt(self):
    # <stmt> --><if_stmt> | <while_loop> | <assignment> | <block>
    if self.currentToken == 'if':
      self.if_stmt()
    elif self.currentToken == 'while':
      self.while_stmt()
    elif self.currentToken == 'id':
      self.assignment()
    elif self.currentToken == '{':
      self.block()
    else:
      self.error()
    pass
  def block(self):
    # block --> `{` {<stmt>';` } `}`
    if self.currentToken == '{':
      self.getNextToken()
      while self.currentToken in ('if', 'while', 'id', '{'):
        self.stmt()
        if self.currentToken == ';':
          self.getNextToken()
        else:
          self.error()
      if self.currentToken == '}':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()
    pass
  def if_stmt(self):
    # <if_stmt> --> `if``(`<bool_expr>`)` <stmt>
    if self.currentToken == 'if':
      self.getNextToken()
      if self.currentToken == '(':
        self.getNextToken()
        self.expr()
        if self.currentToken == ')':
          self.getNextToken()
          self.stmt()
        else:
          self.error()
      pass
    else:
      self.error()
  
  def while_stmt(self):
    # <while_loop> --> `while``(`<bool_expr>`)` <stmt>
    if self.currentToken == 'while':
      self.getNextToken()
      if self.currentToken == '(':
        self.getNextToken()
        self.expr()
        if self.currentToken == ')':
          self.getNextToken()
          self.stmt()
        else:
          self.error()
      pass
    else:
      self.error()
    
  def assignment(self):
    # <assignment> --> `id` `=` <expr>
    if self.currentToken == 'id':
      self.getNextToken()
      if self.currentToken == '=':
        self.getNextToken()
        self.expr()
      else:
        self.error()
    else:
      self.error()
      
  def expr(self):
    # <term> --> <factor> { (+|-) <factor> }
    self.term()
    while self.current() in ('+', '-'):
      self.getNextToken()
      self.term()
  
  def term(self):
    # <term> --> <factor> { (`*` | `/` | '%') <factor> }
    self.factor()
    while self.current() in ('*', '/', '%'):
      self.getNextToken()
      self.factor()
    
  def factor(self):
    '''
    <factor> --> `id` | `int_lit` | `float_lit` `(` <expr> `)`
    FIRST(<factor>) -> {id}{int_lit}{float_lit}{'('}
    '''
    print('current:',self.currentToken)
    if self.currentToken in ('id', 'int_lit', 'float_lit'):
      self.getNextToken()
    elif self.currentToken == '(':
      self.getNextToken()
      self.expr()
      if self.getCurrentToken == ')':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()
  def error(self):
    raise Error('Lexical error detected')
