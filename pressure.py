n = int(input("How many users do you want to enter? "))

for i in range(n):
    print(f"\nEnter details for User {i + 1}")
    Username=input("Enter your username: ")
    Followers=int(input("Enter your number of followers: "))
    verified=input("Are you verified? (yes/no): ")
    rating=float(input("Enter your rating (0.0 to 5.0): "))
    print(f"Username: {Username}")
    print(f"Followers: {Followers}")
    print(f"Verified: {verified}")
    print(f"Rating: {rating}")