# _lock_guard_: Locking mechanism

```cpp
std::lock_guard<std::mutex> lock(mtx);
```

Wherever this line is used, the whole scope in which this line is used, is treated as a critical section.

`mtx` is released when the control exits the scope inside which it is locked.
