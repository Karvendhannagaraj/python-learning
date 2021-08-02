#datatype List

# list is multiple datatype
# list is contain group of element(string, number,..)

#list delaration

list1=["hello",90,90.5,'3rd index'];
print(list1)
#print  using index value
print(list1[0]) #return hello

#print list start from 1 th index value
print(list1[1:]) # retrun  [90, 90.5, '3rd index']

#print list  end with 3rd index value
print(list1[:3]) #return  ['hello', 90, 90.5]

#print  the list start from 1st index to ends with 3rd index
print(list1[1:3]) # return [90, 90.5]

#list multiplication
print(list1*2) # return ['hello', 90, 90.5, '3rd index', 'hello', 90, 90.5, '3rd index']
