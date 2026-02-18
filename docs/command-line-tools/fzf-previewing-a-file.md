# `fzf`: Previewing a file 

```bash
fzf --preview "cat {}"
```

Run this command to get a preview of the file you are looking for.

OR 
This command to preview with syntax highlighting and other features
```bash
fzf --preview "bat --color=always --line-range=:500 {}"
```