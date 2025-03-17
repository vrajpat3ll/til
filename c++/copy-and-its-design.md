# std::copy and its design

std::copy copies [First, Last) to [Dest, ...)

```cpp
OutIt std::copy(InIt First, InIt Last, OutIt Dest)
```

- Basically:
  - std::copy() $\neq$ deep copy
  - std::copy() = "Whatever the copy constructor does"

So if the type has a deep-copying copy constructor, `std::copy()` will behave like a deep copy.

If the type has a shallow-copying copy constructor, `std::copy()` will behave like a shallow copy.

| Type                                             | Use `memcpy`? | Use `std::copy`? | Why?                                |
| ------------------------------------------------ | ------------- | ---------------- | ----------------------------------- |
| POD types (int, float, char, bool, **struct\***) | ✅            | ✅               | Both just copy bytes                |
| Non-POD types (std::string, std::vector)         | ❌            | ✅               | Needs copy constructor to be called |

## How std::copy() Decides What to Do

| State (`Type`)                               | Action by std::copy()              |
| -------------------------------------------- | ---------------------------------- |
| has a copy constructor                       | calls it                           |
| is a POD type                                | copies the raw bytes (like memcpy) |
| it’s copy constructor does _shallow_ copying | performs a _shallow_ copy          |
| it’s copy constructor does _deep_ copying    | effectively performs a _deep_ copy |
