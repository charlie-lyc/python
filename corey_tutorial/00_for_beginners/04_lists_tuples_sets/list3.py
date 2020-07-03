courses = ['History', 'Math', 'Physics', 'Art', 'CompSci']
nums = [1, 5, 2, 4, 3]

courses.remove('Math')
print(courses)
print()

popped = courses.pop() 
print(popped)
print(courses)
print()

courses.reverse()
print(courses)
print()

courses.sort() # -> "sort()" method : sort and store at itself
print(courses)
print()

nums.sort()
print(nums)
print()

courses.sort(reverse=True)
nums.sort(reverse=True)
print(nums)
print(courses)
print()

sorted(courses)
print(courses)
print()

sorted_courses = sorted(courses) # -> "sorted()" function : sort and store at another variable
print(sorted_courses)
print()

print(max(nums))
print(min(nums)) 
print(sum(nums))

