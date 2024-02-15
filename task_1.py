from queue import Queue

queue = Queue()

menu  = ["1. Add new request","2. Pick request from the queue", "0. Exit"]

def generate_request(new_request):
    request = {hash(new_request):new_request}
    queue.put(request)
    return f"\nThe request '{new_request}' was added to the queue. Your unique request number is {request}\n"

def process_request():
    if not queue.empty():
        return f"\nRequest {queue.get()} was picked from the queue and assigned to you.\n"
    else:
        return "\nQueue is empty\n"

print("Hello, to interact with me, please input command number below:\n")
while True:
    for el in menu:
        print(el)
    response = input("\nPlease make your choice:")
    try:

        if int(response) == 1:
            new_request = input("\nInput your request:")
            print(generate_request(new_request))
            continue

        elif int(response) == 2:
            print(process_request())
            continue

        elif int(response) == 0:
            print("Goodbye")
            break

    except:
        print("\nPlease make sure that your input is relevant. Applicable numbers in the menu.\n")