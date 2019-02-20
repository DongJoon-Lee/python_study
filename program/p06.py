# p06-1-hanoi.py

def hanoi(a, b, c, d) :
    
    if a == 1 :
        print(b, '->', c)
        return 
    
    hanoi(a-1, b, d, c)
    print(b, '->', c)
    hanoi(a-1, d, c, b)

print("n = 1")
hanoi(1, 1, 3, 2)
print('n = 2')
hanoi(2, 1, 3, 2)
print('n = 3')
hanoi(3, 1, 3, 2)