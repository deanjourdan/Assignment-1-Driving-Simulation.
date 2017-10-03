Vo = 0
t = int(input("Time: "))
distance = int(input("Distance: "))
speed_limit = 60
a = int(input("acceleration: "))
v = Vo + a*t
s = Vo*t + 1/2*a*t**2

for i in range(t):
    i = i + 1
    s = Vo*i + 1/2*a*i**2
    dis = int(s/10) * '*'
    print("Duration" + str(i) + ':' + "Distance" + " "+str(dis))

if v > speed_limit:
    print('The person went over the speed limit,'+ "" +'Max speed' + str(speed_limit)+ " " + 'm/s')
else:
    print('The person did not go over the speed limit,' + 'Max speed' + str(v)+ " " + 'm/s')

if s >= distance:
    print('The person reached the destination,'+ " " +'Reached'+ " " +str(s), "m")

else:
    print('The person did not reached the destination,'+ " " +'Reached'+ " " +str(s), "m")
