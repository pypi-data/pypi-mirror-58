# BSD 3-Clause License; see https://github.com/jpivarski/awkward-1.0/blob/master/LICENSE

import numbers
import re

import numpy

def wrap(content, namespace):
    import awkward1.layout
    if isinstance(content, awkward1.layout.Content):
        cls = namespace.get(content.type.parameters.get("__class__"))
        if cls is None:
            cls = awkward1.Array
        return cls(content, namespace=namespace)

    elif isinstance(content, awkward1.layout.Record):
        cls = namespace.get(content.type.parameters.get("__class__"))
        if cls is None:
            cls = awkward1.Record
        return cls(content, namespace=namespace)

    else:
        return content

def key2index(keys, key):
    if keys is None:
        attempt = None
    else:
        try:
            attempt = keys.index(key)
        except ValueError:
            attempt = None

    if attempt is None:
        m = key2index._pattern.match(key)
        if m is not None:
            attempt = m.group(0)

    if attempt is None:
        raise ValueError("key {0} not found in record".format(repr(key)))
    else:
        return attempt

key2index._pattern = re.compile(r"^[1-9][0-9]*$")

def minimally_touching_string(limit_length, layout, namespace):
    import awkward1.layout

    if len(layout) == 0:
        return "[]"

    def forward(x, space, brackets=True, wrap=True):
        done = False
        if wrap and isinstance(x, awkward1.layout.Content):
            cls = namespace.get(x.type.parameters.get("__class__"))
            if cls is not None:
                y = cls(x, namespace=namespace)
                if "__repr__" in type(y).__dict__:
                    yield space + repr(y)
                    done = True
        if wrap and isinstance(x, awkward1.layout.Record):
            cls = namespace.get(x.type.parameters.get("__class__"))
            if cls is not None:
                y = cls(x, namespace=namespace)
                if "__repr__" in type(y).__dict__:
                    yield space + repr(y)
                    done = True
        if not done:
            if isinstance(x, awkward1.layout.Content):
                if brackets:
                    yield space + "["
                sp = ""
                for i in range(len(x)):
                    for token in forward(x[i], sp):
                        yield token
                    sp = ", "
                if brackets:
                    yield "]"
            elif isinstance(x, awkward1.layout.Record):
                yield space + "{"
                sp = ""
                for k in x.keys():
                    key = sp + k + ": "
                    for token in forward(x[k], ""):
                        yield key + token
                        key = ""
                    sp = ", "
                yield "}"
            elif isinstance(x, (float, numpy.floating)):
                yield space + "{0:.3g}".format(x)
            else:
                yield space + repr(x)

    def backward(x, space, brackets=True, wrap=True):
        done = False
        if wrap and isinstance(x, awkward1.layout.Content):
            cls = namespace.get(x.type.parameters.get("__class__"))
            if cls is not None:
                y = cls(x, namespace=namespace)
                if "__repr__" in type(y).__dict__:
                    yield repr(y) + space
                    done = True
        if wrap and isinstance(x, awkward1.layout.Record):
            cls = namespace.get(x.type.parameters.get("__class__"))
            if cls is not None:
                y = cls(x, namespace=namespace)
                if "__repr__" in type(y).__dict__:
                    yield repr(y) + space
                    done = True
        if not done:
            if isinstance(x, awkward1.layout.Content):
                if brackets:
                    yield "]" + space
                sp = ""
                for i in range(len(x) - 1, -1, -1):
                    for token in backward(x[i], sp):
                        yield token
                    sp = ", "
                if brackets:
                    yield "["
            elif isinstance(x, awkward1.layout.Record):
                yield "}" + space
                keys = x.keys()
                for i in range(len(keys) - 1, -1, -1):
                    last = None
                    for token in backward(x[keys[i]], ""):
                        if last is not None:
                            yield last
                        last = token
                    if last is not None:
                        yield keys[i] + ": " + last
                    if i != 0:
                        yield ", "
                yield "{"
            elif isinstance(x, (float, numpy.floating)):
                yield "{0:.3g}".format(x) + space
            else:
                yield repr(x) + space

    def forever(iterable):
        for token in iterable:
            yield token
        while True:
            yield None

    halfway = len(layout) // 2
    left, right = ["["], ["]"]
    leftlen, rightlen = 1, 1
    leftgen = forever(forward(layout[:halfway], "", brackets=False, wrap=False))
    rightgen = forever(backward(layout[halfway:], "", brackets=False, wrap=False))
    while True:
        l = next(leftgen)
        if l is not None:
            if leftlen + rightlen + len(l) + (2 if l is None and r is None else 6) > limit_length:
                break
            left.append(l)
            leftlen += len(l)

        r = next(rightgen)
        if r is not None:
            if leftlen + rightlen + len(r) + (2 if l is None and r is None else 6) > limit_length:
                break
            right.append(r)
            rightlen += len(r)

        if l is None and r is None:
            break

    while len(left) > 1 and (left[-1] == "[" or left[-1] == ", [" or left[-1] == "{" or left[-1] == ", {" or left[-1] == ", "):
        left.pop()
        l = ""
    while len(right) > 1 and (right[-1] == "]" or right[-1] == "], " or right[-1] == "}" or right[-1] == "}, " or right[-1] == ", "):
        right.pop()
        r = ""
    if l is None and r is None:
        if left == ["["]:
            return "[" + "".join(reversed(right)).lstrip(" ")
        else:
            return "".join(left).rstrip(" ") + ", " + "".join(reversed(right)).lstrip(" ")
    else:
        if left == ["["] and right == ["]"]:
            return "[...]"
        elif left == ["["]:
            return "[... " + "".join(reversed(right)).lstrip(" ")
        else:
            return "".join(left).rstrip(" ") + ", ... " + "".join(reversed(right)).lstrip(" ")
