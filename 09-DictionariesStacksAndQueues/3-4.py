import queue

def toBin(a):
    binary = queue.LifoQueue()
    while a > 0:
        binary.put(a % 2)
        a = a // 2
    
    output = ''
    while not binary.empty():
        output += str(binary.get())

    return output

print('Natural number: 18')
print(f'Binary number: {toBin(18)}')