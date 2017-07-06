dicDemo = {'name' : 'Sahadat Hossain',
            'address' : 'Nikunjo 2, Khilkhet, Dhaka',
           'university' : 'Northern University Bangladesh',
           'subject' : 'Computer Science and Engineering',
           'home_town' : 'Noakhali',
           'country' : 'Bangladesh'
           }
dicDemo['name'] = 'Sakib'
dicDemo['address'] = 'New York, United State of America'
for x in dicDemo:
    print(str.upper(x),' : ',dicDemo[x])
print('\n'*3)
print(dicDemo.keys())
print('\n'*3)
print(dicDemo.values())
print('\n'*3)
print(len(dicDemo))