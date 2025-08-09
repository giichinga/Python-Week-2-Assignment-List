# Python List Operations Example

This script demonstrates basic list operations in Python, including:

1.  **Appending items** to a list
2.  **Inserting an item** at a specific position
3.  **Extending** a list with another list
4.  **Deleting an item** by index

## Code

``` python
myList = []
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)

print(myList)

myList.insert(1,15)

print(myList)

myList2 = [50, 60, 70]
myList.extend(myList2)

print(myList)

del myList[-1]

print(myList)
```

## Step-by-Step Explanation

1.  **Create an empty list**: `python     myList = []`

2.  **Append items** to the list:
    `python     myList.append(10)     myList.append(20)     myList.append(30)     myList.append(40)`
    Output: `[10, 20, 30, 40]`

3.  **Insert** the number `15` at index `1`:
    `python     myList.insert(1, 15)` Output: `[10, 15, 20, 30, 40]`

4.  **Extend** the list by adding another list:
    `python     myList2 = [50, 60, 70]     myList.extend(myList2)`
    Output: `[10, 15, 20, 30, 40, 50, 60, 70]`

5.  **Delete** the last item from the list: `python     del myList[-1]`
    Output: `[10, 15, 20, 30, 40, 50, 60]`

## How to Run

1.  Save the code to a file, e.g., `myList.py`.
2.  Run it in your terminal: `bash     python myList.py`

## Expected Output

    [10, 20, 30, 40]
    [10, 15, 20, 30, 40]
    [10, 15, 20, 30, 40, 50, 60, 70]
    [10, 15, 20, 30, 40, 50, 60]

------------------------------------------------------------------------

**Author:** Antonny Gichinga
