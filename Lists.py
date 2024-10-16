# Lists

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# ppend e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())

    lst = []

    for i in range(0,N):
        st = input() 
        st1=st.split() 
        
        if st1[0]=='insert': 
            lst.insert(int(st1[1]),int(st1[2]))
        elif st1[0] == 'print':
            print(lst)
        elif st1[0] == 'remove':
            lst.remove(int(st1[1]))
        elif st1[0] == 'append':
            lst.append(int(st1[1]))
        elif st1[0] == 'sort':
            lst.sort()
        elif st1[0] == 'pop':
            lst.pop() 
        elif st1[0] == 'reverse':
            lst.reverse()
