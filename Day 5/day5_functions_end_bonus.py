items2 = ["Mic", "Phone", 321.23, 432.233, "Justin", "Bag", "Cliff tttaaa", 134]

#Wrapping the three above functions into one single function
def sum_and_avg(my_num_list):
    totalsum = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            totalsum += i
    totalcount = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            totalcount += 1
    return "The Sum is: ", totalsum, "Number of items is: ", totalcount, "Average is: ", totalsum / (totalcount * 1.0)

sum_and_avg(items2)
