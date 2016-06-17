from linked_list import LinkedList
# from node import Node


def main():
    ll = LinkedList()

    print("Initial size: ", len(ll))
    ll.push(24)
    print("New size: ", len(ll))
    print("List content: ", ll)
    print("Pushing more")
    ll.push(6)
    ll.push(783)
    print("List content: ", ll)
    print("popping...")
    ll.pop()
    print("List content: ", ll)
    print("Does list contain 24?")
    if ll.contains(24):
        print("Yes")
    else:
        print("No")
    print("Deleting 24")
    ll.delete(24)
    print("List content: ", ll)
    print("Pushing another onto end.")
    ll.append(365)
    print("List content: ", ll)


if __name__ == "__main__":
    main()
