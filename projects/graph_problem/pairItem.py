
# Integer Pairs
# Write a function integerPairs to find and print out all pairs of integers within an input array which sum up to a specified input value k.

# There are multiple ways to do this, depending upon whether you want to favor runtime or space.

# Example:

# input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11

# expected output: '6 5', '7 4', '8 3', '9 2', '10 1'
# Analyze the time and space complexity of your solution.
def findpair(arr, target):
    dict = {}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if target == (arr[i]+arr[j])
                return("found")


def findpair(arr, target):
    for i in range(len(arr)):
        difference = abs(target - arr[i])
        if difference in arr :
            return(arr[i], difference)

def integer_pairs2(arr, num):
   hash = {}
   found = False
   for n in arr:
       if num - n in hash:
           found = True
           print(n, num-n)
       else:
           hash[n] = True
   if not found:
       print("Outta luck sorry.")
        
    

            