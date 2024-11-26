import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

opb = ['(','{','[']
clb = [')','}',']']

matchbr = {
    '(':')',
    '{':'}',
    '[':']'
}

def brackets_ok(expression):
    brackets = queue.LifoQueue()

    for i in expression:

        if i in matchbr.keys():
            brackets.put(i)
        elif i in matchbr.values():
            if not matchbr[brackets.get()] == i:
                return False
        else:
            continue
    return True

if brackets_ok(expression1):
   print('Exp1 ok')
else:
   print('Exp1 not ok')
if brackets_ok(expression2):
   print('Exp2 ok')
else:
   print('Exp2 not ok')
if brackets_ok(expression2):
   print('Exp2 ok')
else:
   print('Exp2 not ok')