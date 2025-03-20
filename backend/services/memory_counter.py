# In-memory counter implementation
current_count = 0  # Global variable

def update_counter(direction):
    """Update the counter based on direction (in/out)"""
    global current_count
    current_count += 1 if direction == "in" else -1
    current_count = max(0, current_count)  # Ensure non-negative
    return current_count

def get_current_count():
    """Get the current value of the counter"""
    global current_count
    return current_count
