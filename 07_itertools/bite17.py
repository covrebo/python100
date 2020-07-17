# Write a function called friends_teams that takes a list of friends, a team_size (type int, default=2) and order_does_matter (type bool, default False).
#
# Return all possible teams. Hint: if order matters (order_does_matter=True), the number of teams would be greater.
#
# See the tests for more details. Enjoy :)

from itertools import permutations, combinations

# friend_list = 'clark ellen audrey russ'.split()
# team_size = 2
# order_does_matter = True

def friends_teams(friend_list, team_size, order_does_matter):
    if order_does_matter:
        return list(permutations(friend_list, team_size))
    else:
        return list(combinations(friend_list, team_size))

# print(friends_teams(friend_list, size, order))
