def ecg_seq_index(n):
    # Checks if two numbers share a factor greater than 1
    def share_factor(x, y):
        min_val = min(x, y)
        for i in range(2, min_val + 1):
            if x % i == 0 and y % i == 0:
                return True
        return False

    # Start the sequence
    sequence = [1, 2]

    # Set of numbers already in the sequence for quick lookup
    included = set(sequence)

    # Current number to add to the sequence
    current = 2

    # Generate sequence until we include 'n'
    while n not in included:
        next_number = None
        candidate = 2  # start looking from the smallest integer greater than 1

        while True:
            if candidate not in included and share_factor(candidate, current):
                next_number = candidate
                break
            candidate += 1

        sequence.append(next_number)
        included.add(next_number)
        current = next_number

    # Return the index of 'n' in the sequence (0-based index)
    return sequence.index(n)

# Example usage:
print(ecg_seq_index(3))  # Output should be 4
print(ecg_seq_index(5))  # Output should be 9
print(ecg_seq_index(7))  # Output should be 13
