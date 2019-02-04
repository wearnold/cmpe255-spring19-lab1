'''
Wayne Arnold's implementation of friends.py functions

Expected output:

Testing num_friends with users 0 and 4:
Hero has 2 friends!
Thor has 2 friends!

Output of sort_by_num_friends:
Dunn has 3 friends!
Sue has 3 friends!
Chi has 3 friends!
Hicks has 3 friends!
Kate has 3 friends!
Hero has 2 friends!
Thor has 2 friends!
Clive has 2 friends!
Devin has 2 friends!
Klein has 1 friend!
'''

users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    friend_count = 0
    for friend_a, friend_b in friendship:
        if friend_a == user['id'] or friend_b == user['id']:
            friend_count += 1
        
    return friend_count


def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    for user in users:
        user['friend_count'] = num_friends(user)
    
    sorted_users = sorted(users, key=lambda k: k['friend_count'],
                          reverse=True)
    
    for user in sorted_users:
        if user['friend_count'] == 1:
            print('%s has %d friend!' % (user['name'], user['friend_count']))
        elif user['friend_count'] != 1:
            print('%s has %d friends!' % (user['name'], user['friend_count']))
    
    return sorted_users

if __name__ == "__main__":
    print('%s has %d friends!' % (users[0]['name'], num_friends(users[0])))
    print('%s has %d friends!' % (users[4]['name'], num_friends(users[4])))

    sort_by_num_friends()
