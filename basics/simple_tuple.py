tpl = ( 3, 6, 9)
lst = [ 12, 15, 18]
tpl = list(tpl)
tpl.extend(lst)
tpl = tuple(tpl)
print(tpl)
print(type(tpl))