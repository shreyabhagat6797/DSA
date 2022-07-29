#Stack

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__top=-1
        self.__elements=[None]*self.__max_size

    def full(self):
        if self.__top==self.__max_size-1:
            return True
        else:
            return False

    def push(self,data):
        if self.full():
            print("Stack is overflow")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def empty(self):
        if self.__top==-1:
            return True
        else:
            return False

    def pop(self):
        if self.empty():
            print("stack is underlow")
        else:
           data=self.__elements[self.__top]
           self.__top-=1
           return data

    def display(self):
        if self.empty():
            print("stack is empty") 
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

s=Stack(5)
s.push("p1")
s.push("p2")
s.push("p3")
s.push(5)
s.push(34)
s.push(4)
print("stack is :")
s.display()
s.pop()
s.pop()
print("stack is :")
s.display()
s.pop()
s.pop()


'''
Given a stack of integers, write a python program that updates the input stack 
such that all occurrences of the smallest values are at the bottom of the stack, 
while the order of the other elements remains the same.

For example:
Input stack (top-bottom) :   5 66  5  8  7
Output:  66  8  7  5  5

'''

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__top=-1
        self.__elements=[None]*self.__max_size

    def full(self):
        if self.__top==self.__max_size-1:
            return True
        else:
            return False

    def push(self,data):
        if self.full():
            print("Stack is overflow")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def empty(self):
        if self.__top==-1:
            return True
        else:
            return False

    def pop(self):
        if self.empty():
            print("stack is underlow")
        else:
           data=self.__elements[self.__top]
           self.__top-=1
           return data

    def display(self):
        if self.empty():
            print("stack is empty") 
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

def change_smallest_value(number_stack):
    l=[]
    while(not number_stack.empty()):
        l.append(number_stack.pop())
    minimum=min(l)
    counter=l.count(min(l))
    for i in range(counter):
        number_stack.push(minimum)
    for element in l[::-1]:
        if element!=minimum:
            number_stack.push(element)
    return number_stack

number_stack=Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("initial stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After updation")
number_stack.display()

#queue

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*max_size
        self.__rear=-1
        self.__front=0

    def full(self):
        if self.__rear==self.__max_size-1:
            return True
        else:
            return False

    def enqueue(self,data):
        if self.full():
            print("overflow")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def empty(self):
        if self.__front>self.__rear:
            return True
        else:
            return False

    def dequeue(self):
        if self.empty():
            print("underflow")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])

q=Queue(5)
q.enqueue(45)
q.enqueue(78)
q.enqueue(8)
#q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()


'''
Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.
Note: A number is said to be evenly divisible if it is divisible by all the numbers in the given range without any remainder. 
Consider the range to be from 1 to 10 (both inclusive).
Assume that there will always be few elements in the input queue, which are evenly divisible by the numbers in the mentioned range.

Example:

Input Queue: 13983, 10080, 7113, 2520, 2500 (front - rear)
Output Queue: 10080, 2520 (front-rear)

'''
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*max_size
        self.__rear=-1
        self.__front=0

    def full(self):
        if self.__rear==self.__max_size-1:
            return True
        else:
            return False

    def enqueue(self,data):
        if self.full():
            print("overflow")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def empty(self):
        if self.__front>self.__rear:
            return True
        else:
            return False

    def dequeue(self):
        if self.empty():
            print("underflow")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])

def check_numbers(number_queue):
    queue1=Queue(5)
    while(not number_queue.empty()):
        status=0
        element=number_queue.dequeue()
        for i in range(1,11):
            if element%i!=0:
               status=1
               break
        if status==0:
            queue1.enqueue(element)
    return queue1

number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)
print("initial queue")
number_queue.display()
print("new queue")
output=check_numbers(number_queue)
output.display()

'''
Given two queues, one integer queue and another character queue, write a python program to merge them to form a single queue.  
Follow the below rules for merging:
•	Merge elements at the same position starting with the integer queue.
•	If one of the queues has more elements than the other, add all the additional elements at the end of the output queue.
Note : max_size of the merged queue should be the sum of the size of both the queues. 

For example,  
Input -- queue1: 3,6,8     queue2: b,y,u,t,r,o
Output -- 3,b,6,y,8,u,t,r,o

'''

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*max_size
        self.__rear=-1
        self.__front=0

    def get_max_size(self):
        return self.__max_size

    def full(self):
        if self.__rear==self.__max_size-1:
            return True
        else:
            return False

    def enqueue(self,data):
        if self.full():
            print("overflow")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def empty(self):
        if self.__front>self.__rear:
            return True
        else:
            return False

    def dequeue(self):
        if self.empty():
            print("underflow")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])

def merged_queue(queue1,queue2):
    queue3=Queue(queue1.get_max_size()+queue2.get_max_size())
    l=queue1.get_max_size()+queue2.get_max_size()
    print(l)
    for i in range(l):
        if not queue1.empty():
            queue3.enqueue(queue1.dequeue())
        if not queue2.empty():
            queue3.enqueue(queue2.dequeue())
    merge_queue=queue3
    return merge_queue

queue1=Queue(3)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)

queue2=Queue(6)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merge_queue=merged_queue(queue1,queue2)
print("the merged queue")
merge_queue.display()

#linked list


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def set_data(self,data):
        self.data=data

    def set_next(self,next):
        self.next=next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add_at_end(self,data):
        new_node=Node(data)    #create new node 
        if self.__head is None:   #if head is empty
            self.__head=self.__tail=new_node  #set ne node as head and tail
            return "element added successfully: "+str(self.__tail.get_data())
        else:  #if not empty
            self.__tail.set_next(new_node)  #set tail next to new node
            self.__tail=new_node     #make nw node as tail node
            return "element added successfully: "+str(self.__tail.get_data())
    
    def add_at_beginning(self,data):
        new_node=Node(data)     #create new node
        new_node.set_next(self.__head)  #set next of new node
        self.__head=new_node   #make new node as head node
        return "data inserted"

    def add_in_between(self,data,data_before):
        new_node=Node(data)  #make new node
        if data_before==None:  #if node_before is not specified
            new_node.set_next(self.__head)  #set head as next node to new node
            self.__head=new_node   #make new node as head node
            if new_node.get_next()==None: #check if list was empty
                self.__tail=new_node  #make new node as tail also
        else:   #if data_before is specified
            node_before=self.find_node(data_before)   #find the node
            if node_before is not None:  #if node before is found
                new_node.set_next(node_before.get_next())   #set next of new node to the next of node before
                node_before.set_next(new_node)   #set the next of node_before to new node
            else:
                print(data_before," is not present in the linked list")

    def find_node(self,data):
        temp=self.__head
        while temp is not None:
            if temp.get_data()==data:
                return temp
            temp=temp.get_next()
        return None

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()

    def delete(self,data):
        node=self.find_node(data)   #find node to be deleted
        if node is not None:   #if data found is not empty
            if node==self.__head: #if node to be deleted is head node
                if self.__head==self.__tail:  #if head node is tail node
                    self.__tail=None  #make tail empty
                self.__head=node.get_next()
            else:
                temp=self.__head
                while temp is not None: #travel to the element
                    if temp.get_next()==node:    #if next element is data to be deleted
                        temp.set_next(node.get_next())  #set before elements next to node
                        if node==self.__tail:     #if element deleted is tail  
                            self.__tail=temp   #set previous element as tail
                        node.set_next(None)  #set nodes next to None
                        break
                    temp=temp.get_next()       #travel next element until it is found
            print("element has been deleted successfully")
        else:
            print(data," is not present in linkedlist")

if __name__=="__main__":
    mylist=LinkedList()
    while True:
        print("Select an option:")
        print("1.Add at end ;2.Add at beginning ;3.add in between ;4.Find node; 5.Delete ;6.display")
        do=int(input("enter your choice: "))
        if do==1:
            data=int(input("enter the element to be inserted: "))
            result=mylist.add_at_end(data)
            print(result)
        elif do==2:
            data=int(input("enter the element to be inserted:"))
            mylist.add_at_beginning(data)
        elif do==3:
            data=int(input("enter the element to be inserted:"))
            data_before=int(input("enter the element before:"))
            resul=mylist.add_in_between(data,data_before)
            print(result)
        elif do==4:
            data=int(input("enter the element to be searched:"))
            result=mylist.find_node(data)
            if result is not None:
                print(result)
            else:
                print("data not found")
        elif do==5:
            data=int(input("enter the element to be deleted:"))
            mylist.delete(data)
        elif do==6:
            mylist.display()
        else:
            print("wrong selection")


'''
Given a linked list of characters. Write a python function to 
return a new string that is created by appending all the characters given in the linked list as per the rules given below.

Rules:

1. Replace '*' or '/' by a single space

2. In case of two consecutive occurrences of '*' or '/' , 
replace those two occurrences by a single space and convert the next character to upper case.

Assume that 

1. There will not be more than two consecutive occurrences of '*' or '/'

2. The linked list will always end with an alphabet

Sample Input	                                                                             Expected Output
 A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y	          An Apple a day Keeps A Doctor Away
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def set_data(self,data):
        self.data=data

    def set_next(self,next):
        self.next=next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add_at_end(self,data):
        new_node=Node(data)    #create new node 
        if self.__head is None:   #if head is empty
            self.__head=self.__tail=new_node  #set ne node as head and tail
            return "element added successfully: "+str(self.__tail.get_data())
        else:  #if not empty
            self.__tail.set_next(new_node)  #set tail next to new node
            self.__tail=new_node     #make nw node as tail node
            return "element added successfully: "+str(self.__tail.get_data())
    
    def add_at_beginning(self,data):
        new_node=Node(data)     #create new node
        new_node.set_next(self.__head)  #set next of new node
        self.__head=new_node   #make new node as head node
        return "data inserted"

    def add_in_between(self,data,data_before):
        new_node=Node(data)  #make new node
        if data_before==None:  #if node_before is not specified
            new_node.set_next(self.__head)  #set head as next node to new node
            self.__head=new_node   #make new node as head node
            if new_node.get_next()==None: #check if list was empty
                self.__tail=new_node  #make new node as tail also
        else:   #if data_before is specified
            node_before=self.find_node(data_before)   #find the node
            if node_before is not None:  #if node before is found
                new_node.set_next(node_before.get_next())   #set next of new node to the next of node before
                node_before.set_next(new_node)   #set the next of node_before to new node
            else:
                print(data_before," is not present in the linked list")

    def find_node(self,data):
        temp=self.__head
        while temp is not None:
            if temp.get_data()==data:
                return temp
            temp=temp.get_next()
        return None

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()

    def delete(self,data):
        node=self.find_node(data)   #find node to be deleted
        if node is not None:   #if data found is not empty
            if node==self.__head: #if node to be deleted is head node
                if self.__head==self.__tail:  #if head node is tail node
                    self.__tail=None  #make tail empty
                self.__head=node.get_next()
            else:
                temp=self.__head
                while temp is not None: #travel to the element
                    if temp.get_next()==node:    #if next element is data to be deleted
                        temp.set_next(node.get_next())  #set before elements next to node
                        if node==self.__tail:     #if element deleted is tail  
                            self.__tail=temp   #set previous element as tail
                        node.set_next(None)  #set nodes next to None
                        break
                    temp=temp.get_next()       #travel next element until it is found
            print("element has been deleted successfully")
        else:
            print(data," is not present in linkedlist")

def create_new_sentence(word_list):
    new_sentence=''
    count=0
    temp=word_list.get_head()
    status=0
    while(temp):
        ch=temp.get_data()
        if ch=='/' or ch=='*':
            new_sentence+=' '
            if temp.get_next().get_data()=='/' or temp.get_next().get_data()=='*':
                status=1
                temp=temp.get_next()
            temp=temp.get_next()
            continue
        if status==1:
            ch=ch.upper()
            status=0
        new_sentence+=ch
        temp=temp.get_next()
    return new_sentence

word_list=LinkedList()
word_list.add_at_end('A')
word_list.add_at_end("n")
word_list.add_at_end('*')
word_list.add_at_end('/')
word_list.add_at_end('a')
word_list.add_at_end('p')
word_list.add_at_end('p')
word_list.add_at_end('l')
word_list.add_at_end('e')
word_list.add_at_end('*')
word_list.add_at_end('a')
word_list.add_at_end('/')
word_list.add_at_end('d')
word_list.add_at_end('a')
word_list.add_at_end('y')

result=create_new_sentence(word_list)
print(result)



'''
The Montessari Public School has planned to organize a cultural evening. The Teacher has framed a schedule based on an idea given by the students.
Assume that the schedule is as below:
Name	Rahul	Sheema	Gitu	Tarun	Tom
Item	Solo Song	Dance	Plays Flute	Gymnastics	MIME
The teacher instructed the children to be ready by holding each other’s hands while standing on the stage and they have to come forward and perform when their turn comes. It is decided that Rahul would perform at the beginning and once again in the middle of the show. After Rahul’s first performance, he would join the other children, in his new position(after Gitu). After Rahul occupies the new position, Swetha would join the children at the end for delivering the vote of thanks.
Assume that there will always be odd number of children initially.
Use the Child class and children_list provided to implement the class Performance as given in the below class diagram.
1. In the constructor of Performance class, initialize children_list
2. Display the schedule
3. Change Rahul’s position after his performance and display the updated schedule
4. Add Swetha and display the updated schedule
__init__(children_list)	 Initializes the children list
change_position(child)	 Used to change the position of the child passed as the argument to the middle position
add_new_child(child)	 Used for adding a new child passed as the argument to the end of the schedule


'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def set_data(self,data):
        self.data=data

    def set_next(self,next):
        self.next=next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add_at_end(self,data):
        new_node=Node(data)    #create new node 
        if self.__head is None:   #if head is empty
            self.__head=self.__tail=new_node  #set ne node as head and tail
            return "element added successfully: "+str(self.__tail.get_data())
        else:  #if not empty
            self.__tail.set_next(new_node)  #set tail next to new node
            self.__tail=new_node     #make nw node as tail node
            return "element added successfully: "+str(self.__tail.get_data())
    
    def add_at_beginning(self,data):
        new_node=Node(data)     #create new node
        new_node.set_next(self.__head)  #set next of new node
        self.__head=new_node   #make new node as head node
        return "data inserted"

    def add_in_between(self,data,data_before):
        new_node=Node(data)  #make new node
        if data_before==None:  #if node_before is not specified
            new_node.set_next(self.__head)  #set head as next node to new node
            self.__head=new_node   #make new node as head node
            if new_node.get_next()==None: #check if list was empty
                self.__tail=new_node  #make new node as tail also
        else:   #if data_before is specified
            node_before=self.find_node(data_before)   #find the node
            if node_before is not None:  #if node before is found
                new_node.set_next(node_before.get_next())   #set next of new node to the next of node before
                node_before.set_next(new_node)   #set the next of node_before to new node
            else:
                print(data_before," is not present in the linked list")

    def find_node(self,data):
        temp=self.__head
        while temp is not None:
            if temp.get_data()==data:
                return temp
            temp=temp.get_next()
        return None

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()

    def delete(self,data):
        node=self.find_node(data)   #find node to be deleted
        if node is not None:   #if data found is not empty
            if node==self.__head: #if node to be deleted is head node
                if self.__head==self.__tail:  #if head node is tail node
                    self.__tail=None  #make tail empty
                self.__head=node.get_next()
            else:
                temp=self.__head
                while temp is not None: #travel to the element
                    if temp.get_next()==node:    #if next element is data to be deleted
                        temp.set_next(node.get_next())  #set before elements next to node
                        if node==self.__tail:     #if element deleted is tail  
                            self.__tail=temp   #set previous element as tail
                        node.set_next(None)  #set nodes next to None
                        break
                    temp=temp.get_next()       #travel next element until it is found
            print("element has been deleted successfully")
        else:
            print(data," is not present in linkedlist")

class Child:
    def __init__(self,name,performance):
        self.__name=name
        self.__performance=performance

    def get_name(self):
        return self.__name

    def get_performance(self):
        return self.__performance

    def __str__(self):
        return self.__name+' '+self.__performance

class Performance:
    def __init__(self,children_list):
        self.__children_list=children_list

    def get_children_list(self):
        return self.__children_list

    def change_position(self,child):
        temp=self.__children_list.get_head()
        temp1=self.__children_list.get_head()
        while temp.get_next():
            temp1=temp1.get_next()
            if temp.get_next().get_next():
                temp=temp.get_next().get_next()
        self.__children_list.delete(child)
        self.__children_list.add_in_between(child,temp1.get_data())

    def add_new_child(self,child):
        temp=self.__children_list.get_head()
        while temp.get_next():
            temp=temp.get_next()
        self.__children_list.add_in_between(child,temp.get_data())

child1=Child("Rahul","solo song")
child2=Child("Sheema","Dance")
child3=Child("Gitu","Plays flute")       
child4=Child("tarun","Gymnastics")
child5=Child("Tom","MIME")

children_list=LinkedList()
children_list.add_at_end(child1)
children_list.add_at_end(child2)
children_list.add_at_end(child3)
children_list.add_at_end(child4)
children_list.add_at_end(child5)

performance=Performance(children_list)
print("initial list of performances:")
performance.get_children_list().display()

print()

print("after Rahul is added in the list after gitu:")
performance.change_position(child1)
performance.get_children_list().display()

print()

child6=Child("Swetha","vote of thanks")
print("after swetha is added to the list:")
performance.add_new_child(child6)
performance.get_children_list().display()


'''
Write a python program to remove all duplicate elements from a sorted linked list containing integer data.
Use the LinkedList class and methods in it to implement the above program.

Example: 
Input LinkedList: 10 10 20 20 30 30 30 40 50
Output LinkedList: 10 20 30 40 50
'''


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def set_data(self,data):
        self.data=data

    def set_next(self,next):
        self.next=next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add_at_end(self,data):
        new_node=Node(data)    #create new node 
        if self.__head is None:   #if head is empty
            self.__head=self.__tail=new_node  #set ne node as head and tail
            return "element added successfully: "+str(self.__tail.get_data())
        else:  #if not empty
            self.__tail.set_next(new_node)  #set tail next to new node
            self.__tail=new_node     #make nw node as tail node
            return "element added successfully: "+str(self.__tail.get_data())
    
    def add_at_beginning(self,data):
        new_node=Node(data)     #create new node
        new_node.set_next(self.__head)  #set next of new node
        self.__head=new_node   #make new node as head node
        return "data inserted"

    def add_in_between(self,data,data_before):
        new_node=Node(data)  #make new node
        if data_before==None:  #if node_before is not specified
            new_node.set_next(self.__head)  #set head as next node to new node
            self.__head=new_node   #make new node as head node
            if new_node.get_next()==None: #check if list was empty
                self.__tail=new_node  #make new node as tail also
        else:   #if data_before is specified
            node_before=self.find_node(data_before)   #find the node
            if node_before is not None:  #if node before is found
                new_node.set_next(node_before.get_next())   #set next of new node to the next of node before
                node_before.set_next(new_node)   #set the next of node_before to new node
            else:
                print(data_before," is not present in the linked list")

    def find_node(self,data):
        temp=self.__head
        while temp is not None:
            if temp.get_data()==data:
                return temp
            temp=temp.get_next()
        return None

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()

    def delete(self,data):
        node=self.find_node(data)   #find node to be deleted
        if node is not None:   #if data found is not empty
            if node==self.__head: #if node to be deleted is head node
                if self.__head==self.__tail:  #if head node is tail node
                    self.__tail=None  #make tail empty
                self.__head=node.get_next()
            else:
                temp=self.__head
                while temp is not None: #travel to the element
                    if temp.get_next()==node:    #if next element is data to be deleted
                        temp.set_next(node.get_next())  #set before elements next to node
                        if node==self.__tail:     #if element deleted is tail  
                            self.__tail=temp   #set previous element as tail
                        node.set_next(None)  #set nodes next to None
                        break
                    temp=temp.get_next()       #travel next element until it is found
            print("element has been deleted successfully")
        else:
            print(data," is not present in linkedlist")

def remove_duplicates(duplicate_list):
    temp=duplicate_list.get_head()
    while(temp.get_next()):
        if temp.get_data()==temp.get_next().get_data():
            temp1=temp
            temp=temp.get_next()
            print("removed:"+str(temp1.get_data()))
            duplicate_list.delete(temp1.get_data())
            continue
        temp=temp.get_next()
    duplicate_list.display()
    return duplicate_list

duplicate_list=LinkedList()
duplicate_list.add_at_end(10)
duplicate_list.add_at_end(10)
duplicate_list.add_at_end(20)
duplicate_list.add_at_end(20)
duplicate_list.add_at_end(30)
duplicate_list.add_at_end(30)
duplicate_list.add_at_end(30)
duplicate_list.add_at_end(40)
duplicate_list.add_at_end(50)

remove_duplicates(duplicate_list)

'''
A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating capacity and the number of passengers.
Write a python program to implement the following:
1. count_compartments()- returns the total number of compartments in the train
2. check_vacancy()- returns the count of the compartments in which more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where data in each node refers to a compartment.

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def set_data(self,data):
        self.data=data

    def set_next(self,next):
        self.next=next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add_at_end(self,data):
        new_node=Node(data)    #create new node 
        if self.__head is None:   #if head is empty
            self.__head=self.__tail=new_node  #set ne node as head and tail
            return "element added successfully: "+str(self.__tail.get_data())
        else:  #if not empty
            self.__tail.set_next(new_node)  #set tail next to new node
            self.__tail=new_node     #make nw node as tail node
            return "element added successfully: "+str(self.__tail.get_data())
    
    def add_at_beginning(self,data):
        new_node=Node(data)     #create new node
        new_node.set_next(self.__head)  #set next of new node
        self.__head=new_node   #make new node as head node
        return "data inserted"

    def add_in_between(self,data,data_before):
        new_node=Node(data)  #make new node
        if data_before==None:  #if node_before is not specified
            new_node.set_next(self.__head)  #set head as next node to new node
            self.__head=new_node   #make new node as head node
            if new_node.get_next()==None: #check if list was empty
                self.__tail=new_node  #make new node as tail also
        else:   #if data_before is specified
            node_before=self.find_node(data_before)   #find the node
            if node_before is not None:  #if node before is found
                new_node.set_next(node_before.get_next())   #set next of new node to the next of node before
                node_before.set_next(new_node)   #set the next of node_before to new node
            else:
                print(data_before," is not present in the linked list")

    def find_node(self,data):
        temp=self.__head
        while temp is not None:
            if temp.get_data()==data:
                return temp
            temp=temp.get_next()
        return None

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()

    def delete(self,data):
        node=self.find_node(data)   #find node to be deleted
        if node is not None:   #if data found is not empty
            if node==self.__head: #if node to be deleted is head node
                if self.__head==self.__tail:  #if head node is tail node
                    self.__tail=None  #make tail empty
                self.__head=node.get_next()
            else:
                temp=self.__head
                while temp is not None: #travel to the element
                    if temp.get_next()==node:    #if next element is data to be deleted
                        temp.set_next(node.get_next())  #set before elements next to node
                        if node==self.__tail:     #if element deleted is tail  
                            self.__tail=temp   #set previous element as tail
                        node.set_next(None)  #set nodes next to None
                        break
                    temp=temp.get_next()       #travel next element until it is found
            print("element has been deleted successfully")
        else:
            print(data," is not present in linkedlist")

class Compartment:
    def __init__(self,compartment_name,no_of_passengers,total_seats):
        self.__compartment_name=compartment_name
        self.__no_of_passengers=no_of_passengers
        self.__total_seats=total_seats

    def get_compartment_name(self):
        return self.__compartment_name

    def get_no_of_passengers(self):
        return self.__no_of_passengers

    def get_total_seats(self):
        return self.__total_seats

class Train:
    def __init__(self,train_name,compartment_list):
        self.__train_name=train_name
        self.__compartment_list=compartment_list

    def get_train_name(self):
        return self.__train_name

    def get_compartment_list(self):
        return self.__compartment_list

    def count_compartments(self):
        temp=self.__compartment_list.get_head()
        count=0
        while(temp):
            count+=1
            temp=temp.get_next()
        return count

    def check_vacancy(self):
        count=0
        temp=self.__compartment_list.get_head()
        while temp:
            vacancy=(temp.get_data().get_total_seats()-temp.get_data().get_no_of_passengers())/temp.get_data().get_total_seats()
            if vacancy>0.5:
                count+=1
            temp=temp.get_next()
        return count

c1=Compartment("Sl",250,400)
c2=Compartment("2AC",150,250)
c3=Compartment("3AC",120,300)
c4=Compartment("FC",160,300)
c5=Compartment("1AC",100,200)

compartment_list=LinkedList()
compartment_list.add_at_end(c1)
compartment_list.add_at_end(c2)
compartment_list.add_at_end(c3)
compartment_list.add_at_end(c4)
compartment_list.add_at_end(c5)

train=Train("Express",compartment_list)
count=train.count_compartments()
print("the total no. of compartments are: ",count)

vacancy_count=train.check_vacancy()
print("no. of compartments vacant more than 50%: ",vacancy_count)