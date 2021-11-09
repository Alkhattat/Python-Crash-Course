#Task 3

#1
first_value = int(input("Type the first value: "))       
second_value = int(input("Type the second value: "))
third_value = (first_value) / (second_value)
print(f"The value of expression for 100/25 is: {third_value}, and its type is {type(third_value)}")


#2
principal = int(input("Enter the value for principal in $: "))
rate = int(input("Enter the value for the rate in percentage: "))
time = int(input("Enter the value for the time in t: "))
simple_interest = (principal) * (rate) * (time) / 100
print (f"Simple interest is {simple_interest}")


#3
first_name = str(input("My first name is :" ))
second_name = str(input("My second name is :" ))
print(f"My full name is {first_name} {second_name}")


#4
boyA = 12
boyB = 13
boyC = 15
boyD = 16
boyE = 19
boyF = 28
add_boys_age = (boyA + boyB + boyC + boyD + boyE + boyF)
avg_age_of_six_boys = (add_boys_age / 6)
print (f"The average age of 6 boys in secondary school is {avg_age_of_six_boys}")


#5
C = float(input("Enter the temperature of Celsius in °C"))
F = (1.8 * C) + 32
print(f"Temperature in Fahrenheit is {F}")

