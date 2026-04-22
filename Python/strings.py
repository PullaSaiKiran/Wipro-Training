Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize
<built-in method capitalize of str object at 0x00000283C37C38A0>
s1.capitalize()
'Hello'
s1.UpperCase()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s1.UpperCase()
AttributeError: 'str' object has no attribute 'UpperCase'
s1.Upper()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s1.Upper()
AttributeError: 'str' object has no attribute 'Upper'. Did you mean: 'upper'?
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='Hello'
s1.casefold()
'hello'
s1.count()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s1.count()
TypeError: count expected at least 1 argument, got 0
s1.count('l')
2
s1.count('h')
0
s1.endswith('o')
True
s1.endswith('o')
True






s1.find('H')
0
s1.index('l')
2
sq.isalpha()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sq.isalpha()
NameError: name 'sq' is not defined. Did you mean: 's1'?
s1.isalpha()
True
s1=isdigit()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s1=isdigit()
NameError: name 'isdigit' is not defined
>>> s1.isdigit()
False
>>> s1.split()
['Hello']
>>> s1.swapcase()
'hELLO'
>>> s1='Hello This Selenium'
>>> s1[1::3]
'eoh li'
>>> s1[::-1]
'muineleS sihT olleH'
>>> 
===================== RESTART: C:/Wipro Training/Python/str1ex.py ====================
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!
>>> 
====================== RESTART: C:/Wipro Training/Python/str2.py =====================
h
>>> 
====================== RESTART: C:/Wipro Training/Python/str2.py =====================
h
e
l
l
o
