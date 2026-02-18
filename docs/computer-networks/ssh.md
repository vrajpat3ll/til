# _SSH_: Cool way to connect to another machine in a local network

I'll focus majorly for Linux machines.

```bash
sudo apt install openssh-server
```

After installing this on your local machine, you can run the following commmand to ssh into
the remote machine
```bash
ssh username@<ip-address>
```

Let's say my username is `vrajpat3ll` and my IPv4 address is 172.12.131.43, 
then you can ssh into my machine using `ssh vrajpat3ll@172.12.131.43`. And voila, you have access to my machine.
Given that you know my machine's password and I've enabled ssh.
