def send_messages(messages):
    while messages:
        sending = messages.pop()
        print(f"Sending message {sending}")
        sent_messages.append(sending)


messages = ['Ja sam mali konj', 'Ti si mala ovca', 'On je mali vo']
sent_messages = []

send_messages(messages[:])

print(messages)
print(sent_messages)
    