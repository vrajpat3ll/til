# Removing write protection from disk / USB drive
## Steps
### Windows

- Press `Win + R`, then type `diskpart.exe` and press enter.
- Enter the following commands.
```
list disk
```
```
select disk X (replace X with the disk you want) 
```
```
attributes disk clear readonly
exit
```

---

Now, try editing the disk or USB drive.

If you still are unable to do so, there could be one or more of the following reasons:
- USB is corrupted
- USB is damaged 
- File system of the USB is not supported


<h5 style="text-align: right;">
    <em>last updated on 8th February, 2025</em>
<h6>
