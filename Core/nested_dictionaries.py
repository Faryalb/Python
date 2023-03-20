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
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)


students = [
         {'first_name':  'Faryal', 'last_name': 'Bhatti'}, # index 0 
         {'first_name': 'Faizan', 'last_name': 'Ausim'}, # index 1
         {'first_name': 'Noor', 'last_name': 'Ausim'}, # index 2
    ]

def iterateDictionary(some_list):
    for s in some_list:
        print('first name - ',s["first_name"],' last name - ',s["last_name"])
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]),i)
        for v in some_dict[i]:
            print(v)
                             
printInfo(dojo)
