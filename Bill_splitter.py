# write your code here
import random
print('Enter the number of friends joining (including you):')
number_friends = int(input())
friends = {}
names = []
if number_friends < 1:
    print("No one is joining for the party")
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(number_friends):
        a = input()
        friends.update({a:0})
        names.append(a)
    print('Enter the total bill value:')
    bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == "Yes":
        name = random.choice(a)
        print(a + ' is the lucky one!')
        try:
            split = bill / (number_friends - 1)
        except ZeroDivisionError:
            print("You have to pay it all bro")
        else:
            friends_split = dict.fromkeys(friends, round(split, 2))
            friends_split.update({a:0})
            print(friends_split)
    else:
        split = bill / number_friends
        friends_split = dict.fromkeys(friends, round(split, 2))
        print('No one is going to be lucky')
        print(friends_split)





