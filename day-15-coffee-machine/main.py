from cm_data import MENU,resources

def m_input(text, poss, err_msg):
    done = False
    while not done:
        ans = input(text)
        if ans in poss:
            done = True
        else:
            print(err_msg)
    return ans



def machine():
    done = False
    poss = ["espresso", "latte", "cappuccino", "report", "off"]
    resources["money"] = 0
    while not done:
        action = m_input("What would you like? ", poss, "Bad entry. Try again.")
        if action == "report":
            report()
        elif action == "off":
            done = True
        else:
            serve(action)

def report():
    for key in resources.keys():
        s = key.title() + ": "
        if key == "money":
            s += "$"
        s += str(resources[key])
        if key in ["milk", "water"]:
            s += "ml"
        elif key == "coffee":
            s += "g"
        print(s)

def serve(action):
    #Check if can do

    #Serve
    item = MENU[action]


    lackingResources = []
    for ing in item["ingredients"]:
        if resources[ing] < item["ingredients"][ing]:
            lackingResources.append(ing)
    if len(lackingResources) == 0:
        print(f"That'll be ${item['cost']}")
        money = get_money()
        if money >= item["cost"]:
            for ing in item["ingredients"]:
                resources[ing] -= item["ingredients"][ing]
            #increase money in resources
            resources["money"] += item["cost"]
            #Give back change
            change = money - item["cost"]
            print("Here's $%.2f in change" % change)
        else:
            print("Sorry, not enough money. Money refunded.")
    else:
        print("Sorry, not enough: " + " ".join(lackingResources))


def get_money():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

machine()