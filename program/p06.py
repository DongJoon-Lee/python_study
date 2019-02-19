# p06-1-hanoi.py
# 입력 : 옮기는 원반의 개수 n, 처음 기둥, 도착점 기둥, 중간기둥
# 출력 : 원반을 옮기는 순서
# 재귀

# def hanoi(a, b, c, d) :
#     # 원반이 1개일 때
#     if a == 1 :
#         print(b, '->', c)
#         return 
    
#     hanoi(a-1, b, d, c)
#     print(b, '->', c)
#     hanoi(a-1, d, c, b)

# print("n = 1")
# hanoi(1, 1, 3, 2)
# print('n = 2')
# hanoi(2, 1, 3, 2)
# print('n = 3')
# hanoi(3, 1, 3, 2)