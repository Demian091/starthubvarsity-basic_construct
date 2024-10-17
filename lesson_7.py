def converter(value_1, value_2):
    sum =float( value_1) + float(value_2)
    num = int(sum)
    try:
        if type(value_1) or type(value_2) == int or float:
            print(num)
        elif type(value_1) or type(value_2) == str or float:
            number = json.loads(value_1)
            num_2 = json.loads(value_2)
            print (num)
        elif value_1 == True:
            return value_1 == 1
            print(num)
        elif value_1 == False:
            return value_1 == 0
        elif value_2 == True:
            return value_2 == 1
            print(num)
        elif value_2 == False:
            return value_2 == 0
    except(TypeError, ValueError):
        print("can't convert value!")
    
# converter('1', 'False')



b =json.loads('')
print(type(b))