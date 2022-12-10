class token:
  def __init__(self, lexeme):
    self.lexeme = lexeme
    self.code = self.look_up(self.lexeme)
  def __str__(self):
    return '<\"{}\", {}>'.format(self.lexeme, self.code)
  def __repr__(self):
    return '{}'.format(self.code)
  def look_up(self, lexeme):
    keywords = [
      'VAR', # indicates variable initialization
      '<FUNCT>', # indicates function initialization
      '<V_ID>', # function / variable names
      '<A_OP>', # assignment operator
      '<REAL>', # real literal, fractional number (float)
      '<NATNUM>', # natural literal, whole numbers and 0 (int)
      '<BOOL>', # boolean (T|F)
      '<CHAR>', # single character
      '<STR>', # string literal
      'IF', # conditional
      '<WHILE>', # while loop
      '<FOR>', # for loop
      '<ADD>', # Addition
      '<SUB>', # Subtraction
      '<MUL>', # Multiplication
      '<DIV>', # Division
      '<POW>',
      '(',
      ')',
      '>',
      '<',
      '>|=',
      '<|=',
      '==',
      '!==',
      'N', # negative numbers formatted as |num|N to seperate from subtraction
      '!',
      '&',
      '|',
      '<B_BLK>', # begin block
      '<E_BLK>', # end block
      'THIS',
      '<EOL>',
      '<S_MLC>', # start mult-line comment
      '<E_MLC>', # end mult-line comment
      '<MLC>', #multi-line comment continued
      '<SLC>', # single-line comment
      '<BARGS>', # char indicating start of argument list for function
      '<A_ID>', # argument identifier
      '<EARGS>', # char indicating end of arguments list
      '<FNAME>' # function name
    ]
    if lexeme in keywords:
      return keywords.index(lexeme)
    else:
      return -1
