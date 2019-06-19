import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        for i in range(1,numUsers+1):
            self.addUser("User"+ str(i))
        #print(f'user {self.users[10].name} {self.lastID}')
        
        #To create N random friendships, create a list with all possible friendship combinations, 
        all = []
        for i in range(1,numUsers+1):
            for j in range(i+1,numUsers+1):
                all.append((i,j))
        print(f' all possible {all}')

        #shuffle the list, then grab the first N elements from the list. 
        #You will need to import random to get shuffle.
        #def fisher_yates_shuffle(l):
        for i in range(0, len(all) - 2):
            random_index = random.randint(i, len(all) - 1)
            swap = all[random_index]
            all[random_index] = all[i]
            all[i] = swap
 
        print(f' all shuffle friend {all} {len(all)}')
        # Create friendships
        for i in range(0,(numUsers*avgFriendships)//2 ):
            userId = all[i][0] 
            friendId = all[i][1]
            self.addFriendship(userId, friendId)
        print(f' hopeful friendship {self.friendships}')

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
print(f' friendships={sg.friendships}')
    # connections = sg.getAllSocialPaths(1)
    # print(f' connection= {connections}')

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([userID])
        while q.size() > 0:
            path = q.dequeue()
            userId = path[-1]
            if userId not in visited:
                visited[userId]=path
                for friend in self.friendships[userId]:
                    if friend not in visited:
                        new_path = path.copy()
                        new_path.append(friend)
                    
                        q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(f' friendships={sg.friendships}')
    connections = sg.getAllSocialPaths(1)
    print(f' connection= {connections}')
