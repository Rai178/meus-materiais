places = ["casa", "vivendas", "atitude"]
places2 = []

def send_messages(msg, sent_message):
    while msg:
        item = msg.pop(0)
        sent_message.append(item)
        print(f"tranfering {item} to new list...")
        print(f"Origin list: {msg}")
        print(f"Destinarion list: {sent_message}")
    
send_messages(places, places2)













