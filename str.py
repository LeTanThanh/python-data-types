if __name__ == "__main__":
  print("I am a string.")
  print(type("I am a string."))

  print('I am too.')
  print(type('I am too.'))

  print("This string contains a single quote (') character.")
  print('This string contains a double quote (") character.')

  print('This string contains a single quote (\') character.')
  print("This string contains a double quote (\") character.")

  print('a\
b\
c')

  print('foo\\bar')

  print('foo\tbar')
  print('foo\abar')
  print('foo\bbar')
  print('foo\fbar')
  print('foo\nbar')
  print('foo\rbar')
  print('foo\tbar')
  print('foo\vbar')

  print('\N{rightwards arrow}')

  print('\141')
  print('\x61')

  print(r'foo\nbar')
  print(R'foo\nbar')

  print('''This string has a single (') and a double (") quote.''')
  print('''This is a
string that spans
across several lines''')
