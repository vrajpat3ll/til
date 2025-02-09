# Learn `yadm`

> [Install here](https://yadm.io/docs/install)

## Usage (similar to `git`)
```shell
# Initialize a new repository
yadm init

# Clone an existing repository
yadm clone <url>

# Add files/changes
yadm add <important file>
yadm commit

# Encrypt your ssh key
echo '.ssh/id_rsa' > ~/.config/yadm/encrypt
yadm encrypt

# Later, decrypt your ssh key
yadm decrypt

# Create different files for Linux vs MacOS
yadm add path/file.cfg##os.Linux
yadm add path/file.cfg##os.Darwin
```