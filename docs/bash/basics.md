# _Basic syntax_: What is it really?

Bash (or Bourne Again SHell) is a command-line interpreter used on Unix-based systems like GNU/Linux.

A bash script is a text file containing a series of commands that you would normally write in a terminal.

It starts out like this:

```bash
#!/bin/bash
echo "Hello, World!"
```

The `#!/bin/bash` is called a shebang. It tells the system to use Bash to interpret the script.

Then, you need to make the script executable. You can do this by running `chmod +x path/to/script.sh` in your terminal.

## Variables

- No spaces around the equal sign (`=`) when declaring variables.
- Use the dollar sign (`$`) to access a variable.
- Use the `read` command to read input into a variable.

Declare a variable like this:

```bash
name="Vraj"
```

Use a variable like this:

```bash
echo "Hello, $name!"
```

Read input into a variable like this:

```bash
echo "Enter your name:"
read user_name
echo "Hello, $user_name!"
```

## Conditionals

Use the syntax below to perform a conditional check:

```bash
if [ $user_name = "Vraj" ]; then
    echo "Welcome back, Vraj!"
else
    echo "Hello, stranger!"
fi
```

You can also compare numbers using the following operators: `-eq`, `-ne`, `-lt`, `-le`, `-gt`, and `-ge`.

## Loops

Use the `for` and `while` loops to iterate over a range of values.

For example:

```bash
for i in {1..5}; do
    echo "Number: $i"
done
```

Or:

```bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

## Function Declaration and Call

Declare a function like this:

```bash
greet() {
    echo "Hello from function!"
}
```

Call a function like this:

```bash
greet
```

Or, you can call a function with arguments:

```bash
greet() {
    echo "Hello, $1!"
}
greet "Vraj"
```

## Additional Syntax Rules:

- You cannot assign a value to a variable inside a quote.
- Bash does not support partial string assignments.
- You cannot use the equal sign (`=`) operator inside an `if` condition.
