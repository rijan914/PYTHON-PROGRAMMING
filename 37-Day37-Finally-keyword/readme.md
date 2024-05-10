# Understanding the `finally` clause in Python

The `finally` clause in Python is used for specifying cleanup actions that must be executed under all circumstances. A `finally` clause is always executed before leaving the `try` statement, whether an exception has occurred or not.

## Why is `finally` needed?

1. **Resource Management**: `finally` is often used for cleanup actions, such as closing files or network connections, regardless of whether an operation succeeded or failed in the `try` block.

2. **Guaranteed Execution**: If an exception is not caught in the `except` block, or if an `except` or `else` clause’s suite contains a `break`, `continue` or `return` statement, the `finally` clause will still be executed before the `try` statement completes.

In the provided code, the `finally` block is used to print "i am always executed", regardless of whether an exception occurred when trying to access an element in the list `l`. This ensures that you always know when the function `fun1` has finished executing, even if it encountered an error.