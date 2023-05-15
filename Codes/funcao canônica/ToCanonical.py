from tt import to_primitives, to_cnf

def to_canonical(expression):
    primitives = to_primitives(expression)
    cnf = to_cnf(primitives)
    return cnf

print(to_canonical('p and q or r'))