import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

"""
Note the order of the printed elements.
The last added element is printed first.
"""

nextcards = [2,3,7,4,1,9,8]

for i in nextcards:
    cards.put(f'{i}')

sum2 = 0
i = 0
while i < 2:
    sum2 += int(cards.get())
    i += 1
print(f'Sum of 2 cards from top: {sum2}')
sumrest = 0
while not cards.empty():
    sumrest += int(cards.get())

print(f'Sum of remaining cards: {sumrest}')