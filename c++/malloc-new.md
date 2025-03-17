# `malloc` vs `new`

Why is this crashing at malloc?

```cpp
template <typename T>
void vector<T>::push_back(T x) {
    if (m_size + 1 > m_capacity) {
        m_capacity = m_capacity << 1;
        T* items = (T*)malloc(m_capacity * sizeof(T));
        if (!items) {
            std::cout << "\e[31mERROR:\e[0m could not allocate memory!\n";
            exit(1);
        }
        print("Allocated memory of %zu bytes!\n", m_capacity);
        memcpy(items, m_items, m_size);
        delete[] m_items;
        m_items = items;
    }
    m_items[m_size++] = x;
}
```

The problem is with this line:

```cpp
memcpy(items, m_items, m_size);
```

## Issues:

- Incorrect memcpy size:

  - memcpy expects the size in bytes, but m_size is likely the number of elements, not the number of bytes.
  - ✅ Correct version:
    ```cpp
    memcpy(items, m_items, m_size * sizeof(T));
    ```

- malloc with new[]/delete[] mismatch:

  - You are using malloc() for allocation but delete[] for deallocation, which is incorrect in C++. malloc() should be paired with free() and new[] should be paired with delete[].

  - ✅ You should either:

    - Replace malloc with new:

    ```cpp
    T* items = new T[m_capacity];
    ```

    - OR replace delete[] with free() (less ideal for C++):

    ```c
    free(m_items);
    ```

- Missing copy constructor call:

      - memcpy is not suitable for objects with non-trivial copy constructors, destructors, or assignment operators. For C++ objects, std::copy() or std::move() should be used instead:

        - ✅ Use std::copy:

```cpp
  std::copy(m_items, m_items + m_size, items);
```

### Fixed Code:

```cpp
template <typename T>
void vector<T>::push_back(T x) {
    if (m_size + 1 > m_capacity) {
        m_capacity = m_capacity << 1;
        T\* items = new T[m_capacity];
        if (!items) {
            std::cout << "\e[31mERROR:\e[0m could not allocate memory!\n";
            exit(1);
        }
        std::copy(m_items, m_items + m_size, items);
        delete[] m_items;
        m_items = items;
    }
    m_items[m_size++] = x;
}
```

### Fixes Summary:

✔️ Use new[] instead of malloc()

✔️ Use std::copy() instead of memcpy() for object copying

✔️ Ensure correct size is passed to memcpy (if using it for POD types)

✔️ Pair new[] with delete[] (or malloc with free)

Ah, got it! The reason lies in how memory allocation works in C++ versus C.

### 🔎 C++ vs C Memory Allocation

#### malloc()

- malloc() comes from C and allocates raw, uninitialized memory.
- It does not call constructors for objects of class types.
- Deallocation is done using free().

#### new[]

- new[] comes from C++ and allocates memory while also calling constructors for objects of class types.
- It sets up the memory properly for C++ objects (including setting up virtual tables, etc.).
- Deallocation is done using delete[].

### 🚨 Why It Crashes

- You allocate memory using malloc() → constructor is NOT called.
- You deallocate using delete[] → delete[] expects that the constructor was called to properly initialize the object.
- Since the constructor wasn’t called, delete[] tries to clean up something that was never initialized → undefined behavior → crash.

### ✅ Solution

- If you use malloc(), pair it with free() — but that means you can’t use class types properly (because constructors won’t be called).
- If you’re working with C++ objects, you should use new[] because it will ensure the constructor is called and the object lifecycle is managed correctly.
- This is why switching to new[] (and delete[]) is the right fix in C++.
