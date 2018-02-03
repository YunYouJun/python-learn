results = []

try:
    f = open('file/scores.txt', encoding='utf-8')
    lines = f.readlines()
    f.close()
except IOError:
    print('File not exists.')

    for line in lines:
        data = line.split()
        sum_score = 0
        for score in data[1:]:
            point = int(score)
            if point < 60:
                continue
            sum_score += point
        result = '%s \t: %d\n' % (data[0], sum_score)
        results.append(result)

print(results)
output = open('file/result.txt', 'w', encoding='utf-8')
output.writelines(results)
output.close()