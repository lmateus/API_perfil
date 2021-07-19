file = open('MonserrateWarp5.csv')

lines = file.readlines()[1:]

dist = []
alt = []
for line in lines:
    info = line.split(',')
    distancia = float(info[0])
    altura = float(info[1])
    dist.append(distancia)
    alt.append(altura)

profile_data = {
    'distancia_x': dist,
    'elevacion': alt
} 


