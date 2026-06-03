import math

data = [[20,500],[40,1000],[30,800],[18,300],[25,1200],[50,1500],[21,1800]]

# initial centers
centers = [[20,50],[40,1000],[30,800]]

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Step 1: grouping
k1 = []
k2 = []
k3 = []

for point in data:
    d1 = distance(point, centers[0])
    d2 = distance(point, centers[1])
    d3 = distance(point, centers[2])
    min_dist = min(d1, d2, d3)
    
    if min_dist == d1:
        k1.append(point)
    elif min_dist == d3:
        k2.append(point)
    else:
        k3.append(point)

print("K1 group:", k1)
print("K2 group:", k2)
print("k3 group:", k3)


# Step 2: new center (mean)
def find_center(cluster):
    x_sum = 0
    y_sum = 0
    
    for p in cluster:
        x_sum += p[0]
        y_sum += p[1]
    
    return [x_sum/len(cluster), y_sum/len(cluster)]

new_c1 = find_center(k1)
new_c2 = find_center(k2)

# print("New Center 1:", new_c1)
# print("New Center 2:", new_c2)