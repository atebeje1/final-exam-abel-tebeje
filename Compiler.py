from Lex import lexer
class compile:
  def __init__(self, path):
    file = open(path, 'r')
    contents = file.readlines()
    self.text = self.toText(contents)
    self.tokens_list = lexer(self.text)
    file.close()
  def toText(self, contents:list) -> str:
    result = ''
    for line in contents:
      result += line
    return result