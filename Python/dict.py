Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

>>> dict={1:10,2:20,3:30}
>>> dict1={1:10,2:20,3:30}
>>> dicr1
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dicr1
NameError: name 'dicr1' is not defined. Did you mean: 'dict1'?
>>> dict1
{1: 10, 2: 20, 3: 30}
>>> dict2={'a':10,'b':20,'c':30}
>>> dict2
{'a': 10, 'b': 20, 'c': 30}
>>> dict2['a']
10
>>> dict2[10]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict2[10]
KeyError: 10
>>> stud={'rno':1001,'sname':'AAA','city':'BBB'}
>>> stud
{'rno': 1001, 'sname': 'AAA', 'city': 'BBB'}
>>> stud['fname']='ccc'
>>> stud
{'rno': 1001, 'sname': 'AAA', 'city': 'BBB', 'fname': 'ccc'}
>>> stud.get('name')
>>> stud.get('sname')
'AAA'
>>> stud.keys()
dict_keys(['rno', 'sname', 'city', 'fname'])
>>> stud.values()
dict_values([1001, 'AAA', 'BBB', 'ccc'])
>>> stud.fromkeys
<built-in method fromkeys of type object at 0x00007FFBD1B59E60>
>>> stud.popitem('AAA')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    stud.popitem('AAA')
TypeError: dict.popitem() takes no arguments (1 given)
