with open('mymodule.py',encoding='UTF-8') as f:
    lines = f.read()

code_obj = compile(lines,'mymodule.py','exec')
exec(code_obj)
