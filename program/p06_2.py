# p06-1-hanoi.py

def hanoi(a, start, end, middle) :
    if a == 1 :
        print(start, '->', end)
        return 
    
    hanoi(a-1, start, middle, end)
    print(start, '->', end)
    hanoi(a-1, middle, end, start)

print('n = 1')
hanoi(1, 1, 3, 2)
print('n = 2')
hanoi(2, 1, 3, 2)
print('n = 3')
hanoi(3, 1, 3, 2)