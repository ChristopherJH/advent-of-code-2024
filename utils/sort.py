def sort(input_list: list):
    i: int = 0
    
    while i < len(input_list) - 1:
        current_val = input_list[i]
        next_val = input_list[i+1]
        # If i and i+1 are the correct way around, continue
        if current_val <= next_val:
            i += 1
            continue
        
        # If i and i+1 aren't the correct way, switch them
        input_list[i] = next_val
        input_list[i+1] = current_val
        
        # Check prev and curr val if switch was made
        if i > 0:
            i -= 1
        
    return input_list