menu={
    "Tea":{
        "ingredients":{
            "milk":100,
            "water":200,
            "coffee":10
            
        },
    "cost":150,
    },
    "espersso":{
        "ingredients":{
            
            "water":50,
            "coffee":20
            
        },
    "cost":200,
    },
    "cappuccino":{
        "ingredients":{
            "milk":150,
            "water":200,
            "coffee":50
            
        },
    "cost":350,
    },
}

    
profit=0
resources={
    "water":500,
    "milk":300,
    "coffee":200
}
is_on=True

def check_resource(order_ingredients):#order ingerdient have list of ingerdient for particular onetea/espersso /....
    for item in order_ingredients:#milk ,coffee,water and it get comapre with resources
        if order_ingredients[item]>resources[item]:
            print(f" sorry there is no enough {item}")
            return False
    return True

def process_coins():
    total=0
    print("plz insert coins")
    conis_five=int(input("How many 5rs coins?:"))
    conis_ten=int(input("How many 10rs coins?:"))
    conis_twenty=int(input("How many 20rs coins?:"))
    total=conis_five*5 + conis_ten*10 + conis_twenty*20
    return total
    
def is_payment_successful(money_recived,coffe_cost):
    if money_recived>=coffe_cost:
        global profit
        profit+=coffe_cost
        change=money_recived-coffe_cost
        print(f"Here is your rs{change} in change")
        return True
    else:
        print(f"sorry that not enough money.money refunded")
        return False
    
    
def make_coffee(coffe_name,coffee_ingeridents):
    for item in coffee_ingeridents:
        resources[item]=resources[item]-coffee_ingeridents[item]
    print(f"Here is your{coffe_name}..enjoyy")

while is_on:
    
    choice=input("what would you like to have?(Tea/espersso/cappuccino)\n Enter 'report' for overall report\nEnter 'off' for exit\n:::")
    if choice=="off":
        is_on=False
    elif choice=="report": #use if becuase off need to check this two
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}g")
        print(f"money={profit}RS")
    else:
        coffee_type=menu[choice]
        print(coffee_type)
        
        if check_resource(coffee_type['ingredients']):#true 
            payment=process_coins()
            if is_payment_successful(payment,coffee_type['cost']):#true only true coffe makeing os going to start
                make_coffee(choice,coffee_type["ingredients"])
            
        
    