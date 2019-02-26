from linkedLists import LinkedList as lk

'''
def choseOption(chose):
    options = {
        1:lk.insertStart(),
        2:lk.insertEnd(),
        3:lk.remove(),
        4:lk.show(),
        5:lk.count(),
        6:lk.countFast()
        }
    
    return options.get(chose, "")

    # for some reason, did not work
'''

def main():

    linked = lk()
    linked.create()

    while(True):
        print("#--------------#")
        print("1. Insert in Start")
        print("2. Insert in End")
        print("3. Remove")
        print("4. Show")
        print("5. Count")
        print("6. Count Fast")
        print("7. Sair")

        chose = int(input("Escolha uma opção: "))

        if chose == 7:
            break
        elif chose == 1:
            linked.insertStart()
        elif chose == 2:
            linked.insertEnd()
        elif chose == 3:
            linked.remove()
        elif chose == 4:
            linked.show()
        elif chose == 5:
            linked.count()
        elif chose == 6:
            linked.countFast()
            
        
if __name__ == "__main__":
    main()
