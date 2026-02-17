# try / except / else / finally relations:
# - The `try` block runs first.
# - If an exception is raised inside `try`, execution jumps to the matching `except`.
# - The `else` block runs only if no exception was raised in `try` (i.e., when `try` succeeds).
# - The `finally` block always runs, regardless of whether an exception occurred or a return happened.
# - Order of possible execution flows:
#   1. try -> else -> finally           (no exception)
#   2. try -> except -> finally         (exception handled)
#   3. try -> except -> finally         (exception raised and not handled here)

try:
    # may raise ValueError (invalid int) or ZeroDivisionError (division by zero)
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except Exception as e:
    # Executes only if an exception was raised in the try block.
    print(f"An error occurred: {e}")
else:
    # Executes only when the try block did NOT raise any exceptions.
    print("No errors occurred.")
finally:
    # Always executes after try/except/else, even if there was a return or another exception.
    print("This block will always execute.")