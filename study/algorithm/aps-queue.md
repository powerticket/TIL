# Algorithm Problem Solving

## Queue

Abstract data type of stacked data

FIFO: First-In, First-Out



### Main operation

enQueue- insert data to the rear of data

deQueue - delete data from the front of data

isEmpty - check the queue is empty or not

isFull - check the queue is full or not

Qpeek - return the item of the front



### Linear queue

#### Implementation

![QueueImplementationUsingCpp](https://java2blog.com/wp-content/uploads/2019/12/QueueImplementationUsingArray.png)

```python
Q = [0] * N
front = rear = -1


def createQ():
    global front, rear
    front = rear = -1
    Q = [0] * N


def enQ(item):
    if isFull():
        return
    rear += 1
    Q[rear] = item

    
def deQ():
    if isEmpty():
        return
    front += 1
	return Q[front]


def isFull():
	return rear == N-1


def isEmpty():
	retrun front == rear


def Qpeek():
    return Q[front+1]
```



### Circular queue

#### Implementation

![Operations-on-Circular queue](https://media.geeksforgeeks.org/wp-content/uploads/Circular-queue_1.png)



