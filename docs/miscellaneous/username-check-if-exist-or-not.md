# Data structures used for string matching and checking for existence in a hashmap

## Tries

- Trees, each node contains a character and a flag to tell if a word ends here or not.
- Is memory efficient compared to normal hashmaps in memory.

## Bloom Filters:

- Hash the string multiple times with different hash fucntions, set the corresponding bit of an array to 1.
- If all bits ON -> Maybe present
- If all bits OFF -> NOT present

![image for comparison](../images/ds-comp-for-username-lookups.png)
