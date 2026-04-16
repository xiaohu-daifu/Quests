class Category:


    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
        return self.check_funds(amount)

    def get_balance(self):
        values = []
        for dic in self.ledger:
            values.append(dic.get('amount',0))
        return sum(values)
    
    def transfer(self, amount,  other):
        if not self.check_funds(amount):
            return False
        
        self.ledger.append({"amount": -amount, "description": f"Transfer to {other.name}"})
        other.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})

        return self.check_funds(amount)

    def check_funds(self, amount) -> bool:
        values = []
        for dic in self.ledger:
            values.append(dic.get('amount',0))

        return (sum(values)  - amount) >= 0

    def __str__(self):
        max_title_len = 30
        
        
        if len(self.name) <= max_title_len:
            
            len_of_title = len(self.name)
            needed_stars = max_title_len - len_of_title
            for_odd_stars = (len_of_title %2 ) * 1

            title = "*" * (needed_stars // 2) + self.name + "*" * (needed_stars // 2 + for_odd_stars)
            #  f"* {* needed_stars // 2} {self.name} *{* needed_stars // 2}"
        else:
            title = self.name[:max_title_len]
        # print(title)
        
        lines = [title]
        
        for dic in self.ledger:
            dic.get("description")
            description = dic.get("description")
            amount = f"{dic.get('amount'):.2f}"
            len_d = len(description)
            len_a = len(amount)
            if len_d <= 23:
                body = description + " " * (30 - len_d - len_a) + amount
                lines.append(body)
            else:
                body = description[:23] + " " * (30 - len_d - len_a) + amount
                lines.append(body) 
        
        # Total
        total = f"Total: {self.get_balance():.2f}"
        lines.append(total)

        return "\n".join(lines)
                    


def create_spend_chart(categories: list):
    print("Percentage spent by category")
    bodie = []
    led_total = []
    for y in range(0, 101, 10):
        bodie += [[y]]
        
    print(bodie)

    for category in categories:
        cat_total = []

        for dic in category.ledger:
            if dic.get("amount") < 0:
                cat_total.append((dic.get("amount")*-1))
        led_total.append(sum(cat_total))
        # print(f"{category.name}: {sum(cat_total)}")
    print((led_total))

    
    for blob in led_total:

        amt = int(round((blob)*100/(sum(led_total)), -1))
        # print(f"amount = {amt}%")
        for i in range(len(bodie)):
            if bodie[i][0] <= amt:
                bodie[i].append("o  ")
            else:
                bodie[i].append("   ")
    
    print(bodie)


    
    for n in range(-1,-12,-1):
        string = ""
        bodie[n].insert(1,"| ")
        if bodie[n][0] == 0:
            bodie[n].insert(0,"  ")
        if bodie[n][0] in range(0,91,10):
            bodie[n].insert(0," ")
        for char in bodie[n]:
            string += str(char)
        print(string)

    print("    -"+"---"*(len(categories)))

# wrote this at 2 am. later learnt there's a max function that normal people use
    # new_bod = ""
    # x = 0
    # if len(categories[0].name) >= len(categories[-1].name):
    #     x = len(categories[0].name)
    #     print(x)
            
    # for a in range(len(categories)-1,0,-1):
    #     if len(categories[a].name) >= len(categories[a-1].name):
    #         if len(categories[a].name) >= x:
    #             x = len(categories[a].name)
    #             print(x)
    
    
    equi_cat = []
    for category in categories:
        if len(category.name) < 20:
            new_name = category.name + " "*(20 - len(category.name))
        else:
            new_name = category.name[:21]
        equi_cat.append(list(new_name))

    
    
    for x in range(20):
        string = "     "
        for cat in equi_cat:
            string += f"{cat[x]}  "
        print(string)

   
            

            
   
        
        
        
        




    
        
        
        
    
    




# tests
food = Category("Food")
food.deposit(2000, "food deposit")
food.withdraw(80, "chicken")
food.withdraw(55, "pizza")

clothes = Category("Clothes")
clothes.deposit(1000)
clothes.withdraw(400, "crop top")
food.withdraw(304)
food.transfer(500, clothes)
clothes.transfer(204, food)

# print(food.ledger)
# print(clothes.ledger)
# print(food.get_balance())
# print(clothes.get_balance())
ent = Category("Entertainment")
tran = Category("Transport")

ent.deposit(1000)
tran.deposit(1000)
ent.withdraw(0)
tran.withdraw(300)
print(clothes)
print(food)
create_spend_chart([clothes, food, ent, tran])