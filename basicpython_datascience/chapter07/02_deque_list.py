import time
from collections import deque

# Stack, Queue 지원
# List보다 효율적인 자료 저장 방식
deque_list1 = deque()
for i in range(5):
    # 기본 리스트 구조라서 append 사용 가능
    deque_list1.append(i)
print(type(deque_list1))
print(deque_list1)
print()

# Queue에 추가
deque_list1.appendleft(10)
print(deque_list1)
print()

# 인덱스 2만큼 증가 시키면서 로테이션
deque_list1.rotate(2)
print(deque_list1)
print()

deque_list1.rotate(2)
print(deque_list1)
print()

print(deque(reversed(deque_list1)))
print()

# 기본 리스트 구조라서 extend 사용 가능
deque_list1.extend([5, 6, 7])
print(deque_list1)
print()

# Queue에 추가 : 추가되는 리스트의 인덱스 0의 값이 결합 부분이 된다.
deque_list1.extendleft([5, 6, 7])
print(deque_list1)
print()


########################################################

# print(time)
# # <module 'time' (built-in)>
# print(type(time))
# # <class 'module'>
# print(dir(time))
# # ['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
# # 'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime',
# # 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time',
# # 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'time_ns',
# # 'timezone', 'tzname', 'tzset']
# print(help(time))
# print()


# Stack Structure : Deque - Linked List
start_time = time.time()
deque_list2 = deque()
for i in range(2000):
    for i in range(2000):
        deque_list2.append(i)
        deque_list2.pop()
print('Deque List :', time.time() - start_time, 'seconds')

# Stack Structure : List - General List
start_time = time.time()
general_list = []
for i in range(2000):
    for i in range(2000):
        general_list.append(i)
        general_list.pop()
print('General List :', time.time() - start_time, 'seconds')
print()
