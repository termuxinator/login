# termux autorun login

username = 'abc'
password = '123'

def login():
  print('')
  while 1:
    print('--- LOGIN ---')
    try:
      u = input('username: ')
      p = input('password: ')
    except KeyboardInterrupt:
      print('')
      print('ctrl-c blocked')
      print('')
      continue
    except EOFError:
      print('')
      print('ctrl-d blocked')
      print('')
      continue
    else:
      if (u == username) and (p == password):
        print('access granted')
        print('')
        return
      else:
        print('access denied')
        print('')
        continue

login()
