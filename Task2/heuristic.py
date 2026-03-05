
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


# same check as brute force - just scanning neighbours
def check_if_arrangement_is_ok(my_arrangement):
    for i in range(len(my_arrangement) - 1):
        left_student = my_arrangement[i]
        right_student = my_arrangement[i + 1]

        if (left_student, right_student) in friend_pairs:
            return False
        if (right_student, left_student) in friend_pairs:
            return False

        if home_city[left_student] == home_city[right_student]:
            return False

    return True


# checks if putting this student next to the last seated person causes any problem
def is_it_safe_to_place_next(already_seated, next_student):
    if not already_seated:
        return True

    last_person_seated = already_seated[-1]

    # would they be sitting next to a friend?
    if (last_person_seated, next_student) in friend_pairs:
        return False
    if (next_student, last_person_seated) in friend_pairs:
        return False

    # would they be next to someone from the same city?
    if home_city[last_person_seated] == home_city[next_student]:
        return False

    return True


# counts how many rules apply to each student
# more rules = harder to place = should go first
def how_many_rules_apply(one_student):
    number_of_friends = sum(
        1 for a, b in friend_pairs
        if a == one_student or b == one_student
    )

    number_from_same_city = sum(
        1 for s in my_classmates
        if s != one_student and home_city[s] == home_city[one_student]
    )

    return number_of_friends + number_from_same_city


# the smart approach - place the most restricted students first
# and skip anyone who would immediately break a rule
def smart_seating(my_classmates):
    print("=" * 55)
    print("   HEURISTIC - placing most restricted students first")
    print("=" * 55)

    # sort so that the students with most constraints go first
    ordered_by_difficulty = sorted(
        my_classmates,
        key=how_many_rules_apply,
        reverse=True
    )

    print("\nStudent difficulty ranking (most restricted first):\n")
    print(f"  {'Name':<12} {'Friends':<10} {'Same City':<12} {'Total'}")
    print("-" * 50)

    for one_student in ordered_by_difficulty:
        num_friends = sum(
            1 for a, b in friend_pairs
            if a == one_student or b == one_student
        )
        num_same_city = sum(
            1 for s in my_classmates
            if s != one_student and home_city[s] == home_city[one_student]
        )
        total = num_friends + num_same_city
        print(f"  {one_student:<12} {num_friends:<10} {num_same_city:<12} {total}")

    print("\nNow placing students one by one...\n")

    seats_filled = []
    still_waiting = ordered_by_difficulty[:]
    total_steps_taken = 0

    while still_waiting:
        someone_was_placed = False

        for candidate in still_waiting:
            total_steps_taken += 1

            if is_it_safe_to_place_next(seats_filled, candidate):
                seats_filled.append(candidate)
                still_waiting.remove(candidate)
                print(f"  Placed {candidate:<10} --> Row so far: {' --> '.join(seats_filled)}")
                someone_was_placed = True
                break
            else:
                print(f"  Skipped {candidate:<9} --> would break a rule")

        # sometimes the heuristic hits a dead end - thats okay
        if not someone_was_placed:
            print("\n  Stuck - no one left can be placed without breaking rules.")
            print("  Heuristic did not find a perfect solution this time.")
            break

    print("\n" + "=" * 55)
    print("FINAL RESULT")
    print("=" * 55)

    arrangement_is_valid = check_if_arrangement_is_ok(seats_filled)

    if arrangement_is_valid and len(seats_filled) == len(my_classmates):
        print(f"\n  Arrangement : {' --> '.join(seats_filled)}")
        print(f"  Valid       : YES")
        print(f"  Steps used  : {total_steps_taken}")
        total_brute_force = 1
        for n in range(1, len(my_classmates) + 1):
            total_brute_force *= n
        print(f"\n  Brute force would need up to {total_brute_force} checks.")
        print(f"  We did it in {total_steps_taken}. Much faster!")
    else:
        print(f"\n  Arrangement : {' --> '.join(seats_filled)}")
        print(f"  Valid       : NO")
        print(f"  Steps used  : {total_steps_taken}")
        print(f"\n  Did not find a perfect answer - but that is")
        print(f"  acceptable for a heuristic. Speed over perfection.")


smart_seating(my_classmates)
