#!/usr/bin/env python3

"""
A filter for parsing quantities expressed inside \Q or \quantity macro e.g.
\Q{1 m/s}, \quantity{9.8 m per second^2} etc.

Requires:
    - pip3 install pint
    - pip3 install panflute
"""

import re
import panflute as P
from pint import UnitRegistry
import itertools

U_ = UnitRegistry()

def searchQuantity(text):
    text = text.strip()
    return [x for x in 
            re.finditer(r'(\\Q|\\quantity)\{(?P<val>\S+)\s+(?P<uexpr>[^}]+)\}'
                , text)]

def formatEval(val, fmt):
    # TODO: Add a cheap test to check if val can be converted to float.
    val = val.lower()
    val = re.sub(r'(1(\.[0]*)?)e', r'e', val)
    if 'e' not in val:
        return val
    a, b = val.split('e')

    # This block return 1e-20 as e-20 to latex and 10~-20~ to markdown. Prefix
    # is removed to save space.
    if not a:
        if fmt == 'latex':
            return f'10^{b}'
        else:
            return f'10^{b}^'

    if fmt == 'latex':
        return val
    else:
        return f'{a}^{b}^'

def _removeUnity(tex):
    # Removes unity prefix. E.g.,
    # - 1e10 -> e10
    # - 1.00e-11 -> e-11
    return re.sub(r'1(\.0*)?e', 'e', tex)

def formatQuantity(qexpr, fmt):
    ms = searchQuantity(qexpr)
    res = []
    if not ms:
        res.append((None, qexpr, False))
        return res
    for m in ms:
        val, uexpr = m.groupdict()['val'], m.groupdict()['uexpr']
        try:
            val = U_(f'{val} {uexpr}')
            res.append((m, val,True))
        except Exception as e:
            P.debug(f'[WARN] Failed to parse {qexpr}. Error: {e}')
            res.append((m, qexpr, False))
    return res

def action_quantity(elem, doc):
    w_ = doc.format
    if isinstance(elem, P.RawInline):
        # Here we have simple replacement of whole string.
        for m, f, success in formatQuantity(elem.text, w_):
            if success:
                if w_ == 'latex':
                    elem.text = _removeUnity(f'{f:Lx}')
                else:
                    elem.text = f'{f:~P}'
                        
    elif isinstance(elem, P.Math) or isinstance(elem, P.RawBlock):
        # Here we have to replace part of the string. A bit more complicated
        # than before. Use gonna use m.span() to find the locations.
        toreplace = []
        for m, f, success in formatQuantity(elem.text, w_):
            if success:
                toreplace.append((m.span(), f))

        noMatch, new = [], []
        prevI, b = 0, 0
        for (a, b), f in toreplace:
            noMatch.append(elem.text[prevI:a])
            f = f'{f:Lx}' if w_ == 'latex' else f'{f:~P}'
            new.append(f)
            prevI = b
        # rest of the text
        noMatch.append(elem.text[b:])
        if toreplace:
            newtext = ''.join(itertools.chain(noMatch, new))
            if elem.text != newtext:
                elem.text = newtext

def main(doc=None):
    P.run_filter(action_quantity, doc=doc)

if __name__ == '__main__':
    main()
