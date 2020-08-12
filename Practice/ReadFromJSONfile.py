import json

# read the file
jsonfile = open('employee.json','r')
jsondata = jsonfile.read()

# parse the data
obj = json.loads(jsondata)

print(str(obj['firstname']))
print(str(obj['lastname']))
print(str(obj['address']))
'''
print(str(obj['address'][0]))
print(str(obj['address'][1]))
'''
list = obj['address']
#print(list)
for item in list:
    print(item)
print('No. of addresses: ', len(list))

for i in range(len(list)):
    print('------------\n ADDRESS of',i+1,'\n------------')
    print("Street: ",list[i].get("street"))
    print("City: ", list[i].get("city"))
    print("State: ", list[i].get("state"))