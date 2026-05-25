#for 循环
>>> seq_lengths = [120, 580, 315, 720, 95]
>>> for aa in seq_lengths:
...     if aa > 500:
... print(f'【警报】: 发现超长蛋白质，长度为 {}')
  File "<stdin>", line 3
    print(f'【警报】: 发现超长蛋白质，长度为 {}')
IndentationError: expected an indented block after 'if' statement on line 2
>>>
>>> for aa in seq_lengths:
...     if aa > 500:
...             print(f'【警报】：发现超长蛋白质，长度为 {aa}')
...
【警报】：发现超长蛋白质，长度为 580
【警报】：发现超长蛋白质，长度为 720
