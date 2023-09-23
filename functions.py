def my_name():
    print("Hello world")
my_name()


def add_sum(a, b):
    answer = a + b
    # print(answer)
    return answer   
    
# add_sum(3, 7)
print("Output", add_sum(3, 7))


# Arbitrary function

def add_nums(*nums):
    sum = 0 
    for num in nums:
        sum += num
    return sum

print("Total Sum", add_nums(3, 4, 6, 8, 9))


def add_ages(**ages):
    age_sum = 0
    for v, k in ages.items():
        age_sum += k
    return age_sum
    
print("Total Ages", add_ages(evans = 25, George = 21, Agnes = 20))













def add_nums(a, b):
    answer = a + b
    
    def double_it():
        double = answer * 2
        print(double)
    double_it()
    
    return answer


print(add_nums(12, 53))



















global_var = 13


def add_nums(a, b):
    
    total = a + b
    print("Global Variable ", global_var)
    
    def double_it():
        #local var
        double = total * 2
        print("Global var in inner function: ", global_var)
        print("Double: ", double)
    double_it()
    
    return total


add_nums(13, 5)