x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
z[0]['y'] = 30
print(x)
print(z)

def last_name_change():
    students[0]['last_name'] = 'Bryant'
    print(students[0] ['last_name'])
last_name_change()

def change_Messi():
    sports_directory['soccer'][0] = 'Andres'
    print(sports_directory['soccer'][0])
change_Messi()



Names = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(Names):
    for name in range(len(Names)):
        print("first_name - "+Names[name]['first_name']+", last_name - "+Names[name]['last_name'])
iterateDictionary(Names)

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name',Names)
iterateDictionary2('last_name',Names)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key in dojo:
        print(len(dojo[key]),key)
        for i in range(len(dojo[key])):
            print(dojo[key][i])
        print("")

printInfo(dojo)
