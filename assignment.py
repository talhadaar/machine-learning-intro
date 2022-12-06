import numpy as np

def get_class_prior(class_name,outcome):
    count=0
    for i in outcome:
        if i==class_name:
            count=count+1
    return count/15
    
def conditional_probability(outcome,class_name,feature_array,value):
    count=0
    a=0
    for i in range(0,15):
        if outcome[i] == class_name:
            a=a+1
        if outcome[i] == class_name and feature_array[i] == value:
            count=count+1
            
    return count/a

# read data
x=np.array([2,4,1,2,4,2,1,2,2,3,3,1,2,4,2])
y=np.array([3,1,3,4,2,1,2,3,2,3,2,2,1,3,2])
z=np.array([2,4,2,3,4,3,4,3,4,3,1,1,4,4,4])
o=np.array([1,2,1,1,2,3,1,2,1,3,1,2,1,3,1])

# a=get_class_prior(1,o)
# b=get_class_prior(2,o)
# c=get_class_prior(3,o)

def predict_class():
    user_input = input("Enter features as space separated string: ")
    user_input = user_input.split(" ")
    user_input = list(map(int, user_input))
    
    a1=conditional_probability(o,1,x,user_input[0])
    b1=conditional_probability(o,1,y,user_input[1])
    c1=conditional_probability(o,1,z,user_input[2])
    likelihood_of_a=a1*b1*c1*8/15

    a2=conditional_probability(o,2,x,user_input[0])
    b2=conditional_probability(o,2,y,user_input[1])
    c2=conditional_probability(o,2,z,4)
    likelihood_of_b= a2*b2*c2*(4/15)

    a3=conditional_probability(o,3,x,user_input[0])
    b3=conditional_probability(o,3,y,user_input[1])
    c3=conditional_probability(o,3,z,user_input[2])
    likelihood_of_c= a3*b3*c3*(3/15)

    prob_of_a_given_condition = likelihood_of_a/(likelihood_of_a+likelihood_of_b+likelihood_of_c)
    prob_of_b_given_condition= likelihood_of_b/(likelihood_of_a+likelihood_of_b+likelihood_of_c)
    prob_of_c_given_condition= likelihood_of_c/(likelihood_of_a+likelihood_of_b+likelihood_of_c)


    result_list = [prob_of_a_given_condition, prob_of_b_given_condition, prob_of_c_given_condition]
    result_dict = dict()
    result_dict[prob_of_a_given_condition] = 'A'
    result_dict[prob_of_b_given_condition] = 'B'
    result_dict[prob_of_c_given_condition] = 'C'

    print("The calculated probabilities: ", result_dict)
    print("Class predicted: ", result_dict[max(result_list)])


predict_class()