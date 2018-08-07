#!usr/bin/python3.5
#join

marxes = ["Groucho", "Chico", "Harpo"];
joinString = ", ".join(marxes);
print(joinString);
marxess = joinString.split(", ");
print(marxess);
print(marxes.insert(0,'asd'))

#sort() sort the list itself
#sorted() returns a sorted copy

marxes = ["Groucho", "Chico", "Harpo"];
sorted_marxes = sorted(marxes);
print("sorted_marxes",sorted_marxes);

print("marxes:",marxes);

marxes.sort();
print("marxes after sort:",marxes);

numbers = [2, 1, 4.0, 3];
numbers.sort();
print("numbers:",numbers);
numbers.sort(reverse=True);
print("numbers reverse",numbers);