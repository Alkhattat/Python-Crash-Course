#Q1. Create a list that contains at least one string, one integer and one float.
my_list = ["Soap", 1200 , 50.5 ]
print(f"The price of {my_list[0]} in the market is #{my_list[1]} and it weight {my_list[2]}kg, therefore, my_list consist of {type(my_list[0])}, {type(my_list[1])} and {type(my_list[2])}")

#Q2. How do I index a nested list? For example I want to grab 2 from [1,1,[1,2]]
my_listB = [1,1,[1,2]]
print(f"One can index a nested list by using multiple indices to reference items within a nested list")
print(f"{my_listB[2][1]}")

#Q3. If lst = [0,1,1]. What is the result of lst.pop()
lst = [0,1,1]
print (f"The result of lst.pop is {lst.pop()}, because pop() removes the last item in the list if no index is specified")

#Q4. List can have multiple objects/data type?
#Yes

#Q5. if lst = ['a','b','c'], what is the result of lst[1:]
lst = ['a','b','c']
print(f"The result of lst[1:] is {lst[1:]}") 

#Q6. When do we choose a list and when do we use dictionary?
print(f"We choose a list whenever we have an ordered collection of items and we use dictionary whenever we have a set of unique keys that map to values.")

#Q7. Create a dictionary with three key value pair
My_dict = {'first_name': 'Murshid', 'Last_name': 'Sulayman', 'Age': 40}
print(My_dict['first_name']) #Example

#Q8. Create a dictionary where all the keys are strings, and all the values are integers.
My_dict2 = {'no_of_people_in_python_crash_course': 11, 'no_of_female_in_the_class': 1, 'no_of_evicted_student':1}
print(My_dict2['no_of_people_in_python_crash_course'])

#Q9. Dictionaries retain order and are a sequence.
print(f"The statement is wrong because dictionary only retain order but its NOT a sequence")

#Q10. Given d = {'k1':[1,2,3]}. What is the output of d['k1'][1]
d = {'k1':[1,2,3]}
print(f"The output of d['k1'][1]  is {d['k1'][1]}")

#Q11. Dictionary are immutable?
print(f"No, they are mutable")

#Q12  d = {'simple_key': 'hello'}. Grab 'Hello'
d = {'simple_key': 'hello'}
print(d['simple_key'])

#Q13 My_dict = {'k1':{'k2': 'Hello'}} ....Grab Hello
My_dict = {'k1':{'k2': 'Hello'}} 
print(My_dict['k1']['k2'])

#Q14 My_dict = {'k1':[{'nest_key':['this is deep',['hello']]}]} ... Grab Hello
My_dict = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(My_dict['k1'][0]['nest_key'][1])

#Q15 My_dict = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}...Grab hello
My_dict = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(My_dict['k1'][2]['k2'][1]['tough'][2][0])