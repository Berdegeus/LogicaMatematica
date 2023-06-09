from typing import List
import re
import sys


class Proposition:
    def __init__(self, value=False):
        self.value = value

    # ->
    def __rshift__(self, rhs):
        return Proposition(not (self.value and not rhs.value))

    # or
    def __add__(self, rhs):
        return Proposition(self.value or rhs.value)

    # and
    def __mul__(self, rhs):
        return Proposition(self.value and rhs.value)

    # not
    def __invert__(self):
        return Proposition(not self.value)

    # <->
    def __eq__(self, rhs):
        return Proposition((self.value and rhs.value) or (not self.value and not rhs.value))

    # ^
    def __ne__(self, rhs):
        return Proposition(self.value != rhs.value)


def getTableElement(s: str, markdown=False, l = -1) -> str:
    l = (len(s) if (l == -1 or markdown == True) else l)
    if markdown:
        s = "$" + s + "$"
    s = s.center(l + 2)
    return s + "|" if markdown else s


def getPropositions(s: str) -> List[str]:
    return list(sorted(set(re.findall(r'\w+', s.replace("T", "").replace("F", "")))))


def getEvalExpression(s: str):
    # not
    s = s.replace("!", "~").replace("not", "~").replace(
        "¬", "~").replace(r"\neg", "~")
    # and
    s = s.replace("&", "*").replace(r"\wedge", "*").replace("and",
                                                            "*").replace("∧", "*")
    # or
    s = s.replace("|", "+").replace(r"\vee", "+").replace("or",
                                                          "+").replace("v", "+").replace("v", "+")
    # <->
    s = s.replace("<->", "==").replace("↔",
                                       "==").replace(r"\leftrightarrow", "==")
    # ->
    s = s.replace("->", ">>").replace("→", ">>").replace(r"\rightarrow", ">>")

    # ^
    s = s.replace("^", "!=").replace("⊕", "!=")
    return s


def getLatexExpression(s: str) -> str:
    return s.replace("~", r" \neg ").replace("*", r" \wedge ").replace(
        "+", r" \vee ").replace("==", r" \leftrightarrow ").replace(">>", r" \rightarrow ").replace("!=", r" \oplus ")


def generateTruthTable(expression: str, reverse=False, markdown=False, file=sys.stdout) -> None:
    # True
    T = Proposition(True)
    # False
    F = Proposition(False)
    # strip
    expression = expression.strip()
    # eval string
    s = getEvalExpression(expression)

    # tautology & conflict
    tautology = True
    conflict = False

    if markdown:
        expression = getLatexExpression(s)

    props = getPropositions(s)
    n = len(props)
    # prop eval buffer
    buf = [Proposition() for i in range(n)] + [T, F]

    if markdown:
        print("|", end='', file=file)

    for i in props + [expression]:
        print(getTableElement(i, markdown=markdown), sep='', end='', file=file)
    print(file=file)
    if markdown:
        print("|", end='', file=file)
        for i in range(n + 1):
            print(" :--: |", end='', file=file)
        print()

    states = range(0, 1 << n)

    for state in reversed(states) if reverse else states:
        if markdown:
            print("|", end='', file=file)
        for i in range(n):
            buf[i].value = (state >> (n - i - 1)) & 1 == 1
            print(getTableElement(
                "FT"[buf[i].value], markdown=markdown, l = len(props[i])), end='', file=file)
        res = eval("(" + s + ").value",{v: buf[i] for i, v in enumerate(props + ['T', 'F'])})
        print(getTableElement("FT"[res], markdown=markdown, l = len(expression)), file=file)
        tautology = tautology and res
        conflict = conflict or res
    if tautology:
        print("\nTautologia.\n", file=file)
    if not conflict:
        print("\nIConflito.\n", file=file)




