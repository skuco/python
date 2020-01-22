foo = int(input('Set the scale: '))
much = int(input('How many numbers?: '))

if foo < 6:
    foo = 6

print('+{0:-^{foo}}+'.format('Table Of Values', foo=foo*4+3))
print('|{0:^{foo}}|{1:^{foo}}|{2:^{foo}}|{3:^{foo}}|'.format('DEC','BIN','OCT','HEX', foo=foo))
print('+{:-^{foo}}+'.format('-', foo=foo*4+3))

for int in range(1,much+1):
    print('|{0:^#{foo}d}|{1:^#{foo}b}|{2:^#{foo}o}|{3:^#{foo}x}|'.format(int, int, int, int, foo=foo ))
    
print('+{:-^{foo}}+'.format('-', foo=foo*4+3))

