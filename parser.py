import re

def parse(code: str):
    if "" in code:
        raise SyntaxError("Character  not allowed in program")
    regex = r"(?P<function>[^{}\n]*?)(?P<data>{(?:(?:.|\n)*?)})"g
    subst = "\\g<0>"
    r = re.sub(regex, subst, test_str, 0).split("")[1:]
    result = [r[0]]
    for x in range(1, len(r)):
        if result[-1][-1] == '\n':
            result.append(r[x])
        else:
            result[-1] += r[x]

    regex2 = r"(?P<function>.*?){(?P<data>(?:.|\n)*)}"
    for x in result:
        m = re.search(regex2, x)
    
