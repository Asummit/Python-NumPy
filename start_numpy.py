import numpy as np

# First method.... #np.array(p_object)
mylist = [1,2,3]
x = np.array(mylist)
print x


# Direct Method
y = np.array([2,4,5])
print y

#2 dimensional array
q = np.array([[136,53,64],[133,564,23]])
print q
print q.shape  #printing the dimension of the ARRAY


#arange(start,stop,step,dtype) funtion
z = np.arange(0,30,2) # arange(START, END, STEP size)
print z

#reshape(a,newshape,order) function
z = z.reshape(3,5)     #reshape(ROW,COLUMN)
print z


#linspace(start,stop, HOW MANY Number we want in return) function
w = np.linspace(0,4,8)
print w


#resize(a, newshape) fuction OR give it matrix dimention you desire like below...
w.resize((3,4))
print w


#resize() another example        #Changing the dimensions of the array.
a = np.array([[0,1],[2,3]])
a = np.resize(a,(2,6))
print a

b = np.ones((3,2))   #creates 1's matrix of 3by2
print b

c = np.zeros((5,2))  #creates 0's matrix of 5by2
print c

d = np.eye((5))  #creates identity matrix of 5by5
print d

e = np.diag(x)  #creates a diagonal matrix of the given NUMPY ARRAY
print e

f = np.array([1,3,2]*4)  #passing a repeated list..
print f

#repeat(a, repeats, axis) function
g = np.repeat([1,2,3],3)  #repeating each element of the list to the given times..
print g


#We can also combine arrays to create new ones. Let's create a two by three array of ones and stack it vertically
# with itself, multiplied by 2. And here's the same thing, but stacking horizontally.

h = np.ones([2,3], int)
#print h                      #adding a matrix of 2 vertically below to the exsisting array
h = np.vstack([h, 2*h])
print h

i = np.ones([2,3], int)
i = np.hstack([i, 2*i])      #adding a matrix of 2 horizontally side to the exsisting array
print i

#Mathematical OPERATIONS, element wise...

j = np.array([1,2,3],float)
k = np.array([4,5,6], float)

print j+k   #Addition

print j*k   #Multiplication

print j**2  #j to the power of 2..

print k/j  #Divison

print k.dot(j) # here  j = [1,2,3] and k = [4,5,6] => [(4.1)+(5.2)+(6.3)] = 14  DOT product

#Let's create a new array using a previous array y and its squared values. The shape of this array is two by three.
l = np.array([j, j**2])
print l
print l.shape


#We can also take the transpose of an array using the T method, which swaps the rows and columns.
# The shape of the transposed array is three by two.
m = l.T
print m
print m.shape

print m.dtype #Type of the Array

m = m.astype('i')   #typecasting of the Array...
print m.dtype

#Some more inbuilt fuctions of NumPy
o = np.array([46,45,21,53,75])   #New Array...

print o.sum()       #SUM of the Array
print o.max()       #Maximum number/value in the Array
print o.min()       #Minimum number/value in the Array
print o.mean()      #Mean value of the Array
print o.std()       #Standard Diviation of the Array
print o.argmax()    #To find the index value of the Maximum Value in the Array... Indexing starts with 0th address..
print o.argmin()    #To find the index value of the Minimum Value in the Array...  Indexing starts with 0th address..


#Indexing/Slicing

p = np.arange(0,13) #an array of squared value of 0 to 12..
print p**2

q = np.arange(13)**2 #Another method
print q

#We can use bracket notation to get the value at a particular index, and the colon notation to get a range.
print q[0], q[2], q[0:7]

print q[1:5]
print q[-4:]

#And here, we're starting fifth from the end, to the beginning of the array,
# and counting backwards by the difference of two.
print q[-5::-2]


#Let's see how this extends to a two-dimensional array. First, let's make a two dimensional array, 0 to 35.
# We can get a specific value by using the comma notation.
# Here's the value at the second row and second column
r = np.arange(36)
r.resize(6,6)
print r
print r[2,2]  #element at 2nd Row- 2nd Column

print r[3, 3:6] #Slice of the 3rd Row.. from column 3 to 6...

print r[:2 , :-2] #Slicing(getting) first 2 rows except the last 2 columns..

print r[-1 , ::2] #Getting every alternate 2nd element from the last Row




# [] operator for Conditional indexing and assignment
r[r>20] #finding all the elements greater than 20 and repalcing them with 30
r[r>20] = 30  #
print r




#Copying element in NumPy
r2 = r[:3, :3] #printing first 3 rows and columns from the orignal array 'r'....
print r2

r2[:] = 0 #Assigning 0's to the sliced array...
print r2

print r   #In the original array that sliced part also becomes 0...

# USE ...r.copy() function is used if we want to create copy of the original array
# and doesn't change the original array..

r_copy = r.copy() #creating the copy of the original array...
print r_copy

r_copy[:] =10
print r_copy
print r         #Notice that the element of the original array has not changed...




#Iterating over Arrays...
#Creating a 4by3 matrix of random numbers from 0to9...
test = np.random.randint(0, 10, (4,3))
print test

for row in test: #iterating by ROW through array...
    print (row)

for i in range(len(test)): #iterating by ROW INDEX...
    print (test [i])

for i, row in enumerate(test): #Enumerate Gives the ROW and the Index of the ROW...
    print('row', i, 'is', row)

test2 = test**2
print test2

#ZIP() fucntion to iterate between 2 Matrix simultaneously...
for i, j in zip(test, test2):
    print(i, '+', j, '=', i+j)


#Using resize and reshape functions to find different patterns of matrix...
s = np.arange(0,36)
#print s
s.resize(6,6)
print s

print s.reshape(36)[::7]
print s[2:4,2:4]

















