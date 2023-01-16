guests_list = set(input() for guest in range(int(input())))
while True:
    command = input()
    if command == "END":
        print(len(guests_list))
        print(*sorted(guests_list), sep="\n")
        break
    guests_list.remove(command)
##############################################################
# OR:
# number_of_guests = int(input())
# guests = set(input() for guest in range(number_of_guests))
# while True:
#     guest = input()
#     if guest == 'END':
#         print(len(guests))
#         print("\n".join(sorted(guests)))
#         break
#     guests.remove(guest)
###############################################################
# OR:
# number_of_guests = int(input())
# guests = set()
# for guest in range(number_of_guests):
#     current_guest = input()
#     guests.add(current_guest)
#
# while True:
#     guest = input()
#     if guest == "END":
#         break
#     guests.remove(guest)
#
# print(len(guests))
# print("\n".join(sorted(guests)))
################################################################

# test inputs:

# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END

# 6
# m8rfQBvl
# fc1oZCE0
# UgffRkOn
# 7ugX7bm0
# 9CQBGUeJ
# 2FQZT3uC
# 2FQZT3uC
# 9CQBGUeJ
# fc1oZCE0
# END
