class ShopingList:
    data = {}
    
    with open("shoppinglist.txt", "r") as file:
        liste = file.readlines()
        for i in liste:
            data[i.split(" ")[0]] = int(i.split(" ")[2])
            
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price
    
    def save_data(self):
        with open("shoppinglist.txt", "w") as file:
            for key, val in self.data.items():
                file.write(key + " — " + str(val) + "\n")
                
    def show_shopping_list(self):
        with open("shoppinglist.txt", "r") as file:
            print(file.read())
        return True
    
    def create(self):
        with open("shoppinglist.txt", "+a") as file:
            file.write(self.name + " — " + str(self.price) + "\n")
            self.data[self.name] = self.price
        
        return self.data
    
    def update(self, old_name: str, old_price: int, new_name: str, new_price: int):
        self.old_name = old_name
        self.old_price = old_price
        self.new_name = new_name
        self.new_price = new_price
    
        for key, val in list(self.data.items()):
            if old_name == key and old_price == val:
                del self.data[key]  
                self.data[new_name] = new_price 
                
                
        self.save_data()
        return True
            
    def delete(self, del_old_name: str, del_old_price: int):
        self.del_old_name = del_old_name
        self.del_old_price = del_old_price
        
        for key, val in list(self.data.items()):
            if self.del_old_name == key and self.del_old_price == val:
                del self.data[key]
                
        self.save_data()
    
    def get_total_price(self):
        sum = 0
        for key, val in self.data.items():
            sum += int(val)
        return sum
        