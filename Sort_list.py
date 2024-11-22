list1=[23,1,16,39]
print(f"First list: {list1}")
list2=[15,90,8,61]
print(f"Second list: {list2}")
merged_list=list1+list2
print(f"Merged list: {merged_list}")
merged_list.sort()
print(f"Sorted list: {merged_list}")
even_numbers=[]
odd_numbers=[]

for num in merged_list:
    even_numbers.append(num) if num%2==0 else odd_numbers.append(num)

final_list=even_numbers+odd_numbers
print(f"Final list: {final_list}")