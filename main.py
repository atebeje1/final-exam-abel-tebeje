import os
from Compiler import compile

for path in os.listdir():
  if path.endswith('abel'):
    result = compile(path)