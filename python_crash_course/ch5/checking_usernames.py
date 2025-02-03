corrent_users = ['valtecir', 'eduardo', 'gilson', 'xavier', 'edivaldo']
new_users = ['Valtecir', 'Eduardo', 'julio', 'arquimedes', 'luiz']
for new_user in new_users:
    if new_user.lower() in corrent_users:
        print(f'you need to enter a new username')
    else:
        print(f'that user is available')
