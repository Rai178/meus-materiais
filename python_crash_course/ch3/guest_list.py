dinner = ['michaela', 'dara', 'debora']
print(f"i'd like to invite you to have a dinner with me {dinner[0]}")
print(f"i'd like to invite you to have a dinner with me {dinner[1]}")
print(f"i'd like to invite you to have a dinner with me {dinner[2]}")
print(f"{dinner[0]}, {dinner[1]} and {dinner[2]} can't do the dinner, then I need to invite other people")
print(len(dinner))
del dinner[0]
del dinner[0]
del dinner[0]
dinner.append('andreia')
dinner.append('jaci')
dinner.append('midiam')
print(f' do you want to have a dinner with me? {dinner[0]}')
print(f' do you want to have a dinner with me? {dinner[1]}')
print(f' do you want to have a dinner with me? {dinner[2]}')
print(len(dinner))
print('I had found a bigger a bigger table!' )
dinner.insert(0, 'valtecir')
dinner.insert(2, 'eduardo')
dinner.insert(-1, 'diego')
print(len(dinner))
print(f' do you want to have a dinner with me? {dinner[0]}')
print(f' do you want to have a dinner with me? {dinner[1]}')
print(f' do you want to have a dinner with me? {dinner[2]}')
print(f' do you want to have a dinner with me? {dinner[3]}')
print(f' do you want to have a dinner with me? {dinner[4]}')
print(f' do you want to have a dinner with me? {dinner[5]}')
print('i can only invite two people for the table, because the dont arrive in time for the dinner ')
popped_dinner = dinner.pop(0)
print(f"sorry {popped_dinner}")
popped_dinner1 = dinner.pop(1)
print(f"sorry {popped_dinner1}")
popped_dinner2 = dinner.pop(2)
print(f"sorry {popped_dinner2}")
popped_dinner3 = dinner.pop(0)
print(f"sorry {popped_dinner3}")
print(len(dinner))
print(f"they are invited for my house to make a love with me {dinner[0]}, and {dinner[1]}")
del dinner[0]
del dinner[0]
print(dinner)