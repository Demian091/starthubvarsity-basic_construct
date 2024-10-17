def condi_func(param):
    value_1 = 5
    if value_1 == param  or not value_1< 10:
        print ('truthy')
    else :
        print('falsy')

#assuming 2 parameters(value_1, value_2) and 1 functional variable (var 1), write a conditional statemenrt that make sure value_1 and var 1 == true
#using >make sure var is > value 2
# the sum of  var and value!1> value 2?/////
# def function_1(var_1):
#     value_1 = 1000000
#     value_2 = 4
#     if var_1 <= value_1:
#         print (True)

# function_1(13)

def funct(param1, param2):
    var1 = 4
    sum = param1 + var1
    if var1 == param1 and var1 > param2 and sum > param2:
        print('''
 param1 = var1
var1 is grater than param2
var1 + param1 ={sum} is greater than param 2
              ''')
    else:
        print('error obliged')
funct(4,2)

Import-Module PSReadLine