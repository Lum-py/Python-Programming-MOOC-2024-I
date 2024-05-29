# write your solution here
def largest():    
    with open("numbers.txt") as file:
        #x = 0
        Values = []
        for i in file:
            Values.append(int(i))
            #if int(i) > int(x):
                #x = i.replace("\n", "")
    return max(Values)
    #return int(x)

if __name__ == "__main":
    largest()