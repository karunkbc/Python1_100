import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

friends_random=random.choice(friends)
print(f"You should pay the bill {friends_random}")

# another way !
random_index=random.randint(0,4)
random_name=friends[random_index]
print(random_name)