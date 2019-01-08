import html

def avg(first, *rest):
    return (first+sum(rest)) / (1+len(rest))

print(avg(1, 2))
print(avg(1, 2, 3, 4, 5))

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
               name=name, 
               attrs=attr_str, 
               value=html.escape(value))
    return element

res = make_element('item', 'Albatross', size='larget', quantity=6)
print(res)

res2 = make_element('p', '<spam>')
print(res2)
