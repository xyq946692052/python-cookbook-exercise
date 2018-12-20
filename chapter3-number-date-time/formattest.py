x = 1234.567890

def showres(num, pat):
    print(format(num, pat))

showres(x, '0.2f')
showres(x, '>10.1f')
showres(x, '<10.1f')
showres(x, '^10.1f')
showres(x, ',')
showres(x, '0,.1f')
showres(x, 'e')
showres(x, '0.2E')

print('The value is {:0,.2f}'.format(x))


