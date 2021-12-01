def ReversePrint(head):
    if head is None:
        return
    ReversePrint(head.next)
    print(head.data)
                    
