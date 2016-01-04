#!/usr/bin/python

def parse(string):
    ret = []
    whitespace = [' ', '\t']

    # Possible states: "new", "int", "str", "fin"
    state = "new"

    current_substr = ""
    for ch in string:
        if state == "new":
            if ch in whitespace:
                # The state continues to be in "new"
                continue
            elif ch == ",":
                raise ValueError("Not expecting a comma just yet")
            elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
                # We just switched to integer parsing mode now
                state = "int"
                current_substr = ch
                continue
            elif ch == '"':
                state = "str"
                current_substr = ""
                continue
            else:
                raise ValueError("Unexpected character: %s" % ch)
        elif state == "int":
            # Expect a digit here
            ord_ch = ord(ch)
            if ord_ch >= ord('0') and ord_ch <= ord('9'):
                current_substr += ch
            elif ch in whitespace:
                ret.append(int(current_substr))
                state = 'fin'
                continue
            elif ch == ',':
                ret.append(int(current_substr))
                state ='new'
                continue
            else:
                raise ValueError('Unexpected character: %s' % ch)
        elif state == "str":
            # Expect a char here
            if ch == '"':
                ret.append(current_substr)
                state = 'fin'
                continue
            else:
                current_substr += ch
            pass
        elif state == 'fin':
            if ch in whitespace:
                continue
            elif ch == ',':
                # We're done
                state = 'new'
                continue
            else:
                raise ValueError("Unexpected character: %s" % ch)
        else:
            raise Exception("Shouldn't come here")

    if state == 'int':
        ret.append(int(current_substr))
    elif state == 'str':
        # This means we never encountered the closing quote
        raise ValueError("Closing quote not found")
    elif state == 'new':
        if len(ret) > 0:
            raise ValueError('Unexpected end of string')
    elif state == 'fin':
        pass

    return ret

print parse('5,6,7')
print parse('5     ,6,7')
print parse('5,6        ,7')
print parse('5        ,         6        ,7')
print parse('5        ,         6        ,7      ')
print parse('           5        ,         6        ,7      ')
print parse('"test", "yoyo","hey, you"')
print parse('"        test", "yoyo","hey, you"')
print parse('         "        test", "yoyo","hey, you"')
print parse('         "        test"       ,   "yoyo", "hey, you"')
#print parse('"test, yoyo, hey')
#print parse('test, yoyo, hey"')
print parse('')
print parse('123')
print parse('"123"')
