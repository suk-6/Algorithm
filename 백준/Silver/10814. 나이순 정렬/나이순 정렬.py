N = int(input())
users = []

for _ in range(N):
    age, name = input().split()
    users.append({"age": int(age), "name": name})
    
users = sorted(users, key=lambda x: x["age"])

for user in users:
    print(user["age"], user["name"])