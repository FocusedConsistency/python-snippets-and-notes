# x or y → Use for defaults. 
# x and y → Use for safe chaining. 
# Leverages short-circuiting for performance and safety.

# ---Setting Default Values---
# The or operator returns the first truthy value, or the last one if all are falsy. This is widely used to provide defaults
name = user_input or "Anonymous"
port = config_port or 8080   

# To preserve falsy values like 0, "", [] use "is not None" instead of "or":
user_count = 0
count = user_count or 10 # Returns 10 - we want 0.
count = user_count if user_count is not None else 10  # Returns 0 — correct!   


# ---Safe Attribute or Function Access---
# Use and to prevent errors when accessing attributes or calling functions
# If obj is None, the second part (obj.value) is not evaluated, avoiding AttributeError
if obj and obj.value > 0:
    print("Valid")

# Stops at the first falsy value — safe and efficient
result = user and user.is_active and user.has_permission()


# ---Avoiding Expensive Operations---
# Short-circuiting skips unnecessary work
# If debug_mode is False, expensive_log() is never called.
if debug_mode and expensive_log():
    print(expensive_log())

