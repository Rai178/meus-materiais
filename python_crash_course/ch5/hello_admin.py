usernames = ['admin', 'xavier', 'joaquim', 'gilson', 'valter']
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'nice to meet you boss!')
        else:
            print(f'{username} have a good day!')
else:
    print(f'We need to find some users')
