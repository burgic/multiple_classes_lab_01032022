class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0

    # def pet_shop_name(self, name):
    #     return self.name

    # def pet_shop_has_cash(self, total_cash):
    #     self.cash == total_cash
    
    # def pets_sold_at_start(self, pets_sold):
    #     pets_sold_at_start = 0
    
    def stock_count(self):
        return len(self.pets)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self,cash):
        self.total_cash += cash

    # def remove_pet(self, pet_to_remove):
    #     index = 0
    #     for pet in self.pets:
    #         if pet == pet_to_remove
    #         self.pet.pop(index)
    #         break
    #     index += 1

    def remove_pet(self, pet):
        self.pets.remove(pet)
    
    def find_pet_by_name(self, name):
        for pet in self.pets:
            if pet.name == name:
                return pet

    def sell_pet_to_customer(self, pet_name, customer):
        pet = self.find_pet_by_name(pet_name)
        customer.reduce_cash(pet.price)
        self.increase_total_cash(pet.price)
        self.increase_pets_sold()
        customer.add_pet(pet)
        self.remove_pet(pet)
        