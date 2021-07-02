# Assignment - 2

#get random names of the people in the list using for loop, Maximum particpant variable and input() function
#and then get your lottery run


import random
maxTicketsAvailable = 10
participants=[]

for i in range (0,maxTicketsAvailable):
  names = input("Enter the participant name: ")
  participants.append(names)


n = random.randint(0,maxTicketsAvailable-1)
print("The winner of this lottery is ",participants[n])
