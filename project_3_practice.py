list = ["dog", "cat", "zebra", "goldfish", "llama"]

#creates and opens file within your pathway 
file = "/DCOBESCIGEEK/test.txt"

with open("test.txt", "a+") as f:
     for item in list:
          f.write(str(item + "\n"))



