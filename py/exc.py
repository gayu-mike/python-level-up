sep = '{}\n'.format('-' * 32)


print('{}EXCEPTION RAISED AND CAUGHT'.format(sep))
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print('{}NO EXCEPTION RAISED'.format(sep))
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print('{}NO EXCEPTION RAISED, WITH ELSE'.format(sep))
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

print('{}EXCEPTION RAISED, BUT NOT CAUGHT'.format(sep))
try:
    x = 1 / 0
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')
