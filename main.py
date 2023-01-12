__winc_id__ = "7599944cfbd94b47beffdbab7a208931"
__human_name__ = "statements"


# Example 1
# Statement with bug


one = 5 % (2 + 3) == 0
two = "Piano"[0:0] == "" + "Guitar"[0:0]
three = 2 ** (3 + 3) - 2 * 11 == 42

print(one, two, three)
