from itertools import permutations

# just a list of students in my class
my_classmates = ["Friend1", "Friend2", "Friend3", "Friend4", "Friend5"]

# these pairs are friends, they cant sit next to each other
friend_pairs = [
    ("Friend1", "Friend3"),
    ("Friend4", "Friend2"),
    ("Friend5", "Friend1")
]

# where each student is from
home_city = {
    "Friend1":   "Kathmandu",
    "Friend2":     "Chitwan",
    "Friend3": "Kathmandu",
    "Friend4":   "Pokhara",
    "Friend5":     "Lalitpur"
}


# goes through the arrangement and checks if any rule is broken
def check_if_arrangement_is_ok(my_arrangement):
    for i in range(len(my_arrangement) - 1):
        left_student = my_arrangement[i]
        right_student = my_arrangement[i + 1]

        # check if they are friends
        if (left_student, right_student) in friend_pairs:
            return False
        if (right_student, left_student) in friend_pairs:
            return False

        # check if they come from the same city
        if home_city[left_student] == home_city[right_student]:
            return False

    return True


# try every single possible order and see which ones work
def try_every_arrangement(my_classmates):
    print("=" * 55)
    print("   BRUTE FORCING....")
    print("=" * 55)

    how_many_tried = 0
    good_arrangements = []

    for one_arrangement in permutations(my_classmates):
        how_many_tried += 1

        if check_if_arrangement_is_ok(one_arrangement):
            good_arrangements.append(one_arrangement)

    print(f"\nNumber of students       : {len(my_classmates)}")
    print(f"Total arrangements tried : {how_many_tried}")
    print(f"Valid ones found         : {len(good_arrangements)}")

    if good_arrangements:
        print("\nArrangements that actually work:")
        for count, arrangement in enumerate(good_arrangements, 1):
            print(f"  {count}. {' --> '.join(arrangement)}")
    else:
        print("\nCould not find any arrangement that works.")

    # showing how fast the number of combinations blows up
    print("\n" + "=" * 55)
    print("How many combinations exist for each class size")
    print("=" * 55)
    print(f"  {'Students':<15} {'Total Combinations'}")
    print("-" * 40)

    running_total = 1
    for n in range(1, 13):
        running_total *= n
        print(f"  {n:<15} {running_total:,}")

    print("\nToo big! Not possible for large number of student in class!")


try_every_arrangement(my_classmates)
