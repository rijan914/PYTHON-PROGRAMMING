# Raising Custom Errors in Python

In Python, we can raise exceptions using the `raise` keyword. This can be a built-in exception such as `ValueError`, `TypeError`, etc., or a custom exception that we define ourselves.

Here's an example from `main.py`:

```python
print("custom errors in python")
a=int(input("enter any value between 5 and 9 "))
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")