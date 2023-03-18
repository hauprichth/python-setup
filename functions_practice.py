def hello():
    print("Hello") 

hello()

item1 = ["shirt", "shoes", "pants"]
item2 = ["camera", "book", "phone"]
item3 = ["tooth brush", "shampoo", "soap"]
def pack(item1, item2, item3):
    print(item1 + item2 + item3)

pack(item1, item2, item3)


my_lunchbox = ['PB&J', 'grapes', 'yogurt', 'cookie']
my_lunchbox2 = []
def eat_lunch():
    for i, ele in enumerate(my_lunchbox):
        if i == 0 :
            print('First I eat ' + ele)
        elif i > 0:
            print('Then I eat ' + ele)
        else: 
            print('My lunchbox is empty!')

eat_lunch()