# queue = []
# queue.append(1)
# queue.append(2)
# queue.append(3)
# # print(queue.pop(0))
# # print(queue.pop(0))
# # print(queue.pop(0))
# while queue:
#     print(queue.pop(0))

# N = 10
# q = [0] * 10
# front = rear = -1
#
# rear += 1
# q[rear] = 10
# rear += 1
# q[rear] = 20
# rear += 1           # enQueue(30)
# q[rear] = 30
# while front != rear:    # 큐가 비어있지 않으면
#     front += 1              # deQueue()
#     print(q[front])


# 덱

from collections import deque

q = []
for i in range(10000):
    q.append(i)
print('append')
while q:
    q.pop(0)
print('end')

dq = deque()
for i in range(10000):
    dq.append(i)
print('append')
while dq:
    dq.pop(0)
print('end')