score = {
    '萧峰': 95,
    '段誉': 97,
    '虚竹': 89,
    '慕容复': 98
}

del score['慕容复']

for name in score:
    print(name, score[name])