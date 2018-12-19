import html

s = 'Elements are written as "<tag>text</tag>".'

print(s)
print(html.escape(s))
print(html.escape(s, quote=False))

print('*'*50)

s = 'Spicy Jalapeño'
res = s.encode('ascii', errors='xmlcharrefreplace')
print(res)

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
