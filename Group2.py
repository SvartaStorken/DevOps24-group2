print("Hello Welcome to Lernia DevOps24 Search tool")
print("Please enter a group number")  #
group = int(input())
if group == 2:
    print ("Wow good pic group 2 was the best in the class")

elif group == 5:
    print ("5 is not a creative number")

elif group > 5:
    print("There are only six groups, try to search for group 2 it is legendary!")
elif group < 0:
    print("The group count starts at 1, try to search for group 2 it is legendary!")
else: 
    print("Sorry there is no information to be found about group " + str(group))
