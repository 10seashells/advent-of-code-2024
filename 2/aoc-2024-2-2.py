
reports = []

def is_safe(report):
    success = True
    prev_level = report[0]
    level = report[1]
    step = prev_level-level

    if step==0 or step<-3 or step>3:
        success = False
    
    prev_level = level
    prev_step = step

    for level in report[2:]:
        step = prev_level-level
        if step==0 or step<-3 or step>3:
            success = False
        elif (step<0 and prev_step>0) or (step>0 and prev_step<0):
            success = False
        prev_level = level
        prev_step = step
    return success

def is_safe_damped(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
        

with open('2/input.txt') as f:
    for line in f.readlines():
        split_line = line.split()
        int_values = []
        for value in split_line:
            int_values.append(int(value))
        reports.append(int_values)

total_safe = 0
for report in reports:
    if is_safe_damped(report):
        total_safe = total_safe + 1

print(total_safe)
