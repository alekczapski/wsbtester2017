"""Zadania z zajec 2018-02-25
"""
import re


def f1(p1, p2=0):
    return p1*p1+p2


def f2(p):
    if len(p) == 0:
        return "BUUUUM"
    else:
        return p[0]


def f3(p):
    d = {1: "jeden", 2: "dwa", 3: "trzy"}
    if p not in d:
        return "other"
    else:
        return d[p]


def f4(p1, p2=""):
    # return ("{0} ma kota" + (" i {1}" if len(p2) > 0 else "")).format(p1, p2)
    return "%s ma kota%s" % (p1, (" i %s" % p2 if len(p2) > 0 else ""))


def f5(p1, p2=1):
    return range(0, p1, p2)


def f6(p1, p2):
    return p1 * p2


def f7(p):
    if re.match(r"^[a-zA-Z]*$", str(p)):
        return "slowo"
    elif re.match(r"^[0-9]$", str(p)):
        return "cyfra"
    elif re.match(r"^[0-9]+$", str(p)):
        return "liczba"
    elif re.match(r"^-[0-9]+$", str(p)):
        return "liczba_ze_znakiem"
    elif re.match(r"^[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+.*$", str(p)):
        return "zdanie"
    elif re.match(r"^<[^/].*>$", str(p)):
        return "tag poczatkowy"
    elif re.match(r"^</.*>$", str(p)):
        return "tag koncowy"


def f8(p1, p2):
    if re.search(str(p1), str(p2)):
        return True
    else:
        return False


def f9(p1, p2):
    if p1 > 0 and p2 > 0:
        return "dodatnie"
    elif p1 < 0 and p2 < 0:
        return "ujemne"
    elif p1 == 0 or p2 == 0:
        return "jest zero"
    elif p1 < 0 < p2 or p1 > 0 > p2:
        return "roznych znakow"


def f10(p1, p2):
    if p1 == p2:
        return "rowne"
    else:
        return "rozne"


def f19(p1, p2):
    if p1 != p2:
        return "rozne"


def f20(p):
    m = re.match(r".*:([0-9]+)", p)
    if m:
        return str(m.group(1))


def f100(p):
    m = re.search(r"<tag>(?!<tag>)(.*?)</tag>", p)
    if m:
        return str(m.group(1))
