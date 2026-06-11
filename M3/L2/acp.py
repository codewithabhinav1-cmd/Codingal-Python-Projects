def shutdown(status):
    if status == "yes":
        return "Shutting down"
    elif status == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

# Example
print(shutdown("yes"))
print(shutdown("no"))
print(shutdown("abc"))