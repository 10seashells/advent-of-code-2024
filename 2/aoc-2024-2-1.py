
reports = []

with open('2/input.txt') as f:
    for line in f.readlines():
        split_line = line.split()
        int_values = []
        for value in split_line:
            int_values.append(int(value))
        reports.append(int_values)

total_safe = 0
for report in reports:
    failure = False
    prev_level = report[0]
    level = report[1]
    step = prev_level-level

    if step==0 or step<-3 or step>3:
        failure = True
    
    prev_level = level
    prev_step = step

    for level in report[2:]:
        step = prev_level-level
        if step==0 or step<-3 or step>3:
            failure = True
        elif (step<0 and prev_step>0) or (step>0 and prev_step<0):
            failure = True
        prev_level = level
        prev_step = step
    if failure == False:
        total_safe = total_safe + 1

print(total_safe)
