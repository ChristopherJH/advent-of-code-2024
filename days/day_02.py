def calculate_num_of_safe_reports(reports: list[list[int]]):
    num_of_safe_reports = 0

    for _, report in enumerate(reports):
        if is_report_safe(report):
            num_of_safe_reports += 1

    return num_of_safe_reports


def is_report_safe(report: list[int]):
    is_increasing = report[0] < report[1]
    if not is_difference_safe(report[0] - report[1]):
        return False

    for j in range(0, len(report) - 1):
        difference = report[j + 1] - report[j]
        if is_difference_safe(difference) and is_direction_safe(
            difference, is_increasing
        ):
            continue
        else:
            return False

    return True


def is_difference_safe(difference: int):
    if difference == 0 or abs(difference) > 3:
        return False
    return True


def is_direction_safe(difference: int, is_increasing: bool):
    return difference > 0 if is_increasing else difference < 0


def calculate_num_of_safe_reports_with_dampener(reports: list[list[int]]):
    num_of_safe_reports = 0

    for _, report in enumerate(reports):
        if is_report_safe(report):
            num_of_safe_reports += 1
        else:
            for i, _ in enumerate(report):
                safe_report = list(report)
                safe_report.pop(i)
                if is_report_safe(safe_report):
                    num_of_safe_reports += 1
                    break

    return num_of_safe_reports
