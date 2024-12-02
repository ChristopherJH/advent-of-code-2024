def calculate_num_of_safe_reports(reports: list[list[int]]):
    num_of_unsafe_reports = 0
    
    for _, report in enumerate(reports):
        if report[0] == report[1]:
            num_of_unsafe_reports += 1
            continue
        
        is_increasing = report[0] < report[1]
        for j in range(0, len(report) - 1):
            difference = report[j+1] - report[j]
            if is_increasing and (difference <=0 or difference > 3):
                num_of_unsafe_reports += 1
                break
            
            if not is_increasing and (difference >= 0 or difference < -3):
                num_of_unsafe_reports += 1
                break
            
    return len(reports) - num_of_unsafe_reports
                
                
                
    