def displayInventory(inv):
    # for i in inv.items():
        # print(i)
    for i, j in inv.items():
        print(i, ':', j)


def addInventory(inv, addItems):
    for i in addItems:
        if i == 'rope':
            inv['rope'] = inv['rope'] + 1
        elif i == 'gold coin':
            inv['gold coin'] = inv['gold coin'] + 1
        elif i == 'rope':
            inv['rope'] = inv['rope'] + 1
        elif i == 'torch':
            inv['torch'] = inv['torch'] + 1
        elif i == 'dagger':
            inv['dagger'] = inv['dagger'] + 1
        else:
            print()


# inventory
Inventory = {'rope': 0, 'gold coin': 0, 'rope': 0, 'torch': 0, 'dagger': 0}
addItem1 = ['rope', 'rope']
addInventory(Inventory, addItem1)

displayInventory(Inventory)

