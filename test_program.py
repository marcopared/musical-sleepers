import sleeper

data = []

graph_data = open('test.txt', 'r').read()
lines = graph_data.split('\n')

for line in lines:
    if len(line) > 1:
        x, y = line.split(',')
        data.append(float(x))
        data.append(float(y))

print(data)
sleeper.liveplot(data, 1000, 1500)
