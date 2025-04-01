# Signals

```cpp
signal(SIGINT, handle_sigint);
```

## What does this line do?

- `SIGINT`:

  - SIGINT (Signal Interrupt) is a signal sent to a process when the user presses `Ctrl+C` in the terminal.
  - By default, this signal terminates the process.

- `signal(SIGINT, handle_sigint);`:
  - This registers a custom _signal handler_ function, `handle_sigint`, to be executed when the SIGINT signal is received.
  - Instead of terminating the process immediately, the program will call handle_sigint() when Ctrl+C is pressed.

Example Usage:

```cpp
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_sigint(int sig) {
    printf("\nCaught signal %d (SIGINT). Ignoring Ctrl+C.\n", sig);
}

int main() {
    signal(SIGINT, handle_sigint);

    while (1) {
        printf("Running... Press Ctrl+C to test signal handling.\n");
        sleep(2);
    }

    return 0;
}
```

- The `handle_sigint` function is called when `Ctrl+C` is pressed.
- Instead of terminating the program, it prints a message.
- The `while (1)` loop keeps the program running.

> [!TIP]
> If better signal handling (like resetting behavior after handling) is required, use `sigaction()` instead of `signal()`, as `signal()` behavior can be inconsistent across systems.
