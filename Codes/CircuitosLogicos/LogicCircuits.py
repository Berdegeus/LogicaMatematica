Op = input('input:')
result = ('')


if Op == ('P^Q'):
    result = ('~(Pv~Q)')

elif Op == ('PvQ'):
    result = ('~(P^~Q)')

elif Op == ('P <> Q'):
    result = ('(P^Q)v(~P^~Q)')

elif Op == ('P -> Q'):
    result = ('~PvQ')

elif Op == ('P <-> Q'):
    result = ('(P^Q)v(~P^~Q)')

elif Op == ('P xor Q'):
    result = ('(PvQ)^~(P^Q)')

elif Op == ('P nor Q'):
    result = ('~(PvQ)')

elif Op == ('P nand Q'):
    result = ('~(P^Q)')

elif Op == ('P and Q'):
    result = ('~(PvQ)')

elif Op == ('P or Q'):
    result = ('~(P^Q)')

else:
    result = ('Invalid operator')

print (result)