def messenger(messages, sent_messages):
    """ Simulate sending a message. """
    while messages:
        message = messages.pop()
        print(f"Sending message: {message}")
        sent_messages.append(message)

def show_sent_messages(sent_messages):
    """ Show all the messages that were sent. """
    print("\nThe following messages were sent:")
    for sent_message in sent_messages:
        print(sent_message)

messages = ['message', 'random message', 'something else', 'okay']
sent_messages = []

# call the function messenger with a *copy* of the list[:] messages to demo how to retain the list
messenger(messages[:], sent_messages)
show_sent_messages(sent_messages)

# print both of your lists to show that the original list has retained its messages 
print(f"\n--- List Summary ---")
print(f"Messages List: {messages}")
print(f"Sent Messages List: {sent_messages}")