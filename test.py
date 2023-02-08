import csv
def new_start():
    print("1. To Show the member list.")
    print("2. To ADD the member.")
    print("3. To see the whole  member.")
    choose = int(input("Choose as you want in 1, 2, 3 :"))


    if choose == 1:
        class Member:
            def __init__(self,name,Id,Rank):
                self.name = name
                self.Id = Id
                self.Rank = Rank

            def update_Rank(self,new_Rank):
                self.Rank = new_Rank

        def write_to_file(members):
            with open('member.csv','w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'Id', 'Rank'])
                for member in members:
                    writer.writerow([member.name, member.Id, member.Rank])

        def read_from_file():
            members = []
            with open('member.csv', 'r')as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    name,Id,Rank = row
                    members.append(Member(name, Id, Rank))
            return members
        member1 = Member("Alan", "TM10001", "Gold 500")
        member2 = Member("Brittany","TM10002","Ordinary 0")


        write_to_file([member1,member2])

        members = read_from_file()
        for member in members:
            print(member.name,member.Id, member.Rank)
            
    elif choose == 2:
        
    
        add = input("What is your new member's name : ")
        add1 = input("Input - ID :")
        add2 = input("Input - Member's Point : ")
        with open('member.csv','a')as file:
            file.write(f"{add}, {add1}, {add2}\n")


    elif choose == 3:
        with open('member.csv','r') as file:
            print(file.read())
        

    




def play_again():
    answer = input("Do you wanna make the member management? yes or no :")
    
    if answer == "y" or answer == "yes" or answer == "Yes":
        return True
    else:
        return False

while play_again():
    new_start()

print("Bye")
