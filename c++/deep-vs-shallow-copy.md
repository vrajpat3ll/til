# Shallow Copy vs Deep Copy

## Shallow Copy:

- A shallow copy means copying the object’s pointers but not the underlying data they point to.
- After a shallow copy:
  - Both objects share the same underlying data.
  - If one object modifies the data, the other object sees the change.
  - When one object is destroyed, the other object may become invalid → double free or dangling pointer issues.

```cpp
class Shallow {
public:
    int* data;

    Shallow(int value) {
        data = new int(value);
    }

    ~Shallow() {
        delete data;
    }
};

Shallow a(42);
Shallow b = a; // Shallow copy – both objects share the same `data`
```

## Deep Copy:

- A deep copy means creating a completely independent copy of the object, including any dynamically allocated memory.
- After a deep copy:
  - Each object has its own copy of the data.
  - Modifying one object does NOT affect the other.
  - Destruction of one object doesn't affect the other.

```cpp
class Deep {
public:
    int* data;
    // ...
    Deep(int value) { data = new int(value); }
    ~Deep() { delete data; }

    // Deep copy constructor
    Deep(const Deep& other) {
        data = new int(*other.data); // Create new memory and copy value
    }
};

Deep a(42);
Deep b = a; // Deep copy – separate memory for `data`
```
