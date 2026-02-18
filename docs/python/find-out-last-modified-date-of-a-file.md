# Find out last modified date of a file

```python
import os, time

file_path = 'path/to/your/file.txt'

# Get the last modified timestamp
timestamp = os.path.getmtime(file_path)

# Convert the timestamp to a readable date and time
modified_date = time.ctime(timestamp)
```