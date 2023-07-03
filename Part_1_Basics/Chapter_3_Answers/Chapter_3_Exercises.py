#---------------------------------------------#
#-- PYTHON CRASH COURSE CHAPTER 3 EXERCISES --#
#---------------------------------------------#
#   
# -- Author: Tony Gutierrez
# -- Date: 05/21/2023 
# -- Tools used: Python, VS Code

# These are the answers to the Chapter 3 exercises on Python Crash Course, 2nd Edition by Eric Matthes

# Problem 3.1: This code creates a list of friends and then accessess each element in the list, one at a time
print("Problem 3.1")
friends = ["Bernard", "Cesar", "Art", "Sean", "Fry"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])



############################################################################################################################
# Problem 3.2: This code creates a list of friends and then writes a greeting message to each element in the list
print("Problem 3.2")
friends = ["Bernard", "Cesar", "Art", "Sean", "Fry"]
print(f"What's up, {friends[0]}?")
print(f"What's up, {friends[1]}?")
print(f"What's up, {friends[2]}?")
print(f"What's up, {friends[3]}?")
print(f"What's up, {friends[4]}?")



############################################################################################################################
# Problem 3.3: This code creates a list of modes of transportation and prints statements about these items
print("Problem 3.3")
vehicles = ["Honda electric car", "Harley Davidson motorcycle", "helicopter"]
print(f"I would like to own a {vehicles[0]}.")
print(f"I would like to own a {vehicles[1]}.")
print(f"I would like to own a {vehicles[2]}.")



############################################################################################################################
# Problem 3.4: This code creates a guest list and writes a message to each person inviting them to dinner
print("Problem 3.4")
guest_list = ['lady gaga', 'albert einstein', 'michael jordan', 'dwayne johnson']
print(f"Hi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")



############################################################################################################################
# Problem 3.5: This code creates a guest list and writes a message to each person inviting them to dinner. 
# Then it modifies the list because a guest can't make it
print("Problem 3.5")
guest_list = ['lady gaga', 'albert einstein', 'michael jordan', 'dwayne johnson']
print(f"Hi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")

print(f"\nIt seems that {guest_list[0].title()} can't make it to dinner tomorrow")
guest_list[0] = 'jimi hendrix'
print(f"\nHi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")



############################################################################################################################
# Problem 3.6: This code creates a guest list and writes a message to each person inviting them to dinner. 
# Then it modifies the list because a guest can't make it.  Also, it adds three new guests
# to dinner and sends a new set of invitations to them
print("Problem 3.6")
guest_list = ['lady gaga', 'albert einstein', 'michael jordan', 'dwayne johnson']
print(f"Hi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")

print(f"\nIt seems that {guest_list[0].title()} can't make it to dinner tomorrow")
guest_list[0] = 'jimi hendrix'
print(f"\nHi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")

print(f"\nI found a bigger table.  That means I can invite more people for dinner tomorrow.")
guest_list.insert(0, 'jim carrey')
guest_list.insert(2, 'oprah winfrey')
guest_list.append('charles barkley')

print(f"\nHi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[4].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[5].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[6].title()}, please come to my home for dinner tomorrow.")



############################################################################################################################
# Problem 3.7: This code creates a guest list and writes a message to each person inviting them to dinner. 
# Then it modifies the list because a guest can't make it.  Also, it adds three new guests
# to the guest list and sends a new set of invitations to them. Finally, it removes names
# from the list due to space limitations, resends invitations to the two guests, and deletes
# the list objects, showing proof at the end
print("Problem 3.7")
guest_list = ['lady gaga', 'albert einstein', 'michael jordan', 'dwayne johnson']
print(f"Hi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")

print(f"\nIt seems that {guest_list[0].title()} can't make it to dinner tomorrow")
guest_list[0] = 'jimi hendrix'
print(f"\nHi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")

print(f"\nI found a bigger table.  That means I can invite more people for dinner tomorrow.")
guest_list.insert(0, 'jim carrey')
guest_list.insert(2, 'oprah winfrey')
guest_list.append('charles barkley')

print(f"\nHi {guest_list[0].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[4].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[5].title()}, please come to my home for dinner tomorrow.")
print(f"Hi {guest_list[6].title()}, please come to my home for dinner tomorrow.")

print(guest_list)
removed_guest = guest_list.pop()
print(f"\nI am sorry, {removed_guest.title()}, but I can't invite you to my home for dinner because my table is not big enough")
removed_guest = guest_list.pop()
print(f"I am sorry, {removed_guest.title()}, but I can't invite you to my home for dinner because my table is not big enough")
removed_guest = guest_list.pop()
print(f"I am sorry, {removed_guest.title()}, but I can't invite you to my home for dinner because my table is not big enough")
removed_guest = guest_list.pop()
print(f"I am sorry, {removed_guest.title()}, but I can't invite you to my home for dinner because my table is not big enough")
removed_guest = guest_list.pop()
print(f"I am sorry, {removed_guest.title()}, but I can't invite you to my home for dinner because my table is not big enough")

print(f"\nYou are still invite, {guest_list[0].title()}.")
print(f"Your are still invited, {guest_list[1].title()}.")

del guest_list[0]
del guest_list[0]
print(guest_list)



############################################################################################################################
# Problem 3.8: This code creates an unsorted list of cities I would like to visit. Then I 
# print the list without sorting the list data. Then I print the original
# list to show the original order. Then I print the list in reverse alphabetical
# order without sorting the list data. Then I print the list oritinal list to
# show the original order. Then I use the reverse method to change the order of 
# the list. Then I use the reverse method again to change the order of the list.
# Then I use the sort method to change the order of the list alphabetically.
# Finally, I use the sort method to change the order of the list to reverse 
# alphabetical order
print("Problem 3.8")
like_to_visit = ["paris", "mexico city", "san jose", "seoul", "dublin", "buenos aires"]
print("This is the list's original order:")
print(like_to_visit)

print("\nThis is the sorted order, without changing the actual data on the list:")
print(sorted(like_to_visit))

print("\nThis is the list's original order again to prove that the data is intact:")
print(like_to_visit)

print("\nThis is the reverse sorted order, without changing the actual data on the list:")
print(sorted(like_to_visit, reverse=True))

print("\nThis is the list's original order again to prove that the data is intact:")
print(like_to_visit)

print("\nThis is the list's reverse order using the reverse() method:")
like_to_visit.reverse()
print(like_to_visit)

print("\nThis is the list's original order again:")
like_to_visit.reverse()
print(like_to_visit)

print("\nThis is the list's sorted order using the sort() method, so the list data is permanently changed:")
like_to_visit.sort()
print(like_to_visit)

print("\nThis is the list's reverse alphabetical sorted order using the sort() method, so the list data is permanently changed:")
like_to_visit.sort(reverse=True)
print(like_to_visit)



############################################################################################################################
# Problem 3.9: This code checks the length of the guest list used for Problem 3.6
print("Problem 3.9")
guest_list = ['jim carrey', 'jimi hendrix', 'oprah winfrey', 'albert einstein', 'michael jordan', 'dwayne johnson', 'charles barkley']
print(f"The number of people invited to dinner on Problem 3.6 is {len(guest_list)}")



############################################################################################################################
# Problem 3.10: This code creates a list of Japanese mountains and performs the functions used in this chapter once
print("Problem 3.10")
jpn_mountains = ['mount fuji', 'mount tate', 'mount ibuki', 'mount tsurugi']
print(jpn_mountains[0])
print(jpn_mountains[1].title())
msg = f"\nThe first mountain I hiked was {jpn_mountains[2].title()}."
print(msg)
jpn_mountains[3] = 'mount daisen'
print(jpn_mountains)
jpn_mountains.append('mount rokko')
print(jpn_mountains)
jpn_mountains.insert(0, 'mount maya')
print(jpn_mountains)
del jpn_mountains[0]
print(jpn_mountains)
pop_jpn_mountains = jpn_mountains.pop(0)
print(f"\nMy favorite Japanese mountain is {pop_jpn_mountains.title()}.")
jpn_mountains.remove('mount tate')
print(jpn_mountains)
jpn_mountains.sort()
print(jpn_mountains)
jpn_mountains.sort(reverse=True)
print(jpn_mountains)
jpn_mountains.reverse()
print(jpn_mountains)