# Method Resolution Order (MRO)

This is the order in which python's interpreter searches classes to find a method or attribute.

It is really important when using multiple inheritance, because a method might exist in multiple parent classes.

### Simple Example 

```py
class A:
	def greet(self):
		print("A")

class B(A):
	pass
 
class C(B):
	pass

c = C()
c.greet()
```

python searches: C->B->A and finds greet() in A.

See the MRO using C.mro() -> [<class '__main__.C'>,
<class '__main__.B'>,
<class '__main__.A'>,
<class 'object'>]


## How Python Computes MRO

Python uses the C3 Linearization Algorithm.

It guarantees:

- Children come before parents.
- The order specified in the inheritance list is respected.
- A class appears only once in the MRO.

## MRO and super()

super() doesn't mean 'call the parent'. It means call the next class in the MRO. 
Each super() moves to the next class in MRO, not necessarily the direct parent.
