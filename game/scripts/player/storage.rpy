init python:
    all_items = []
    rarity_list = ["common", "uncomon", "rare", "very rare", "epic", "legendary", "sdfpasdofasdpjfosaidfajspdofij"]
    # 1=1 legendary    2/5=4 epic  6/12=7 very rare   8/23=15 rare  24/49=25uncomon 49/50=commom

    def check_rarity(number):
        if number == 1:
            return 5
        elif number >=2 and number <=4:
            return 4
        elif number >=6 and number<=15:
            return 3
        elif number >=8 and number<=23:
            return 2
        elif number >= 24 and number<= 49:
            return 1
        elif number >= 50:
             return 0

    class Inventoryx(object):

        def __init__(self, items):
            self.items = items

        def add_item(self, id, quantity):
            item_index = self.item_exists(id)
            # mc (str(item_index))
            if item_index != -1:
                self.items[item_index].add_quantity(quantity)
            else:
                self.items.append(ItemReference(id, quantity))

        def remove_item(self,id, quantity):
            item_index = self.item_exists(id)
            if item_index == -1:
                return
            if not self.item_necessary_quantity(item_index, quantity):
                return
            self.items[item_index].remove_quantity(quantity)
            if self.items[item_index].quantity == 0:
                reference_to_index = self.items[item_index]
                del self.items[item_index]
                # self.items.remove(item_index)

        def item_necessary_quantity(self, item_index, quantity):
            if self.items[item_index].quantity >= quantity:
                return True
            return false

        def item_exists(self, this_id):
            item_index = -1
            for item in self.items:
                item_index += 1
                if item.id == this_id:
                    return item_index
            return -1

        def clear_all(self):
            for i in range(len(self.items)):
                del self.items[0]

        def transfer_all(self, target):
            for i in range(len(self.items)):
                target.add_item(self.items[0].id, self.items[0].quantity)
                del self.items[0]
                # mc ("len = " + str(len(self.items)))

        def list_items(self):
            for this_item in self.items:
                mc ("id = " + str(this_item.id) + " quantity = " + str(this_item.quantity))



    class InventoryItem(object):
        def __init__(self, id, name, max_quantity, type, is_active, buy_price, sell_price, rarity, description):
            self.id = id
            self.type = type
            self.name = name
            self.is_active = is_active
            self.buy_price = buy_price
            self.sell_price = sell_price
            self.rarity = rarity
            self.description = description
            self.add_to_all_items_list()

        def add_to_all_items_list(self):
            for item in all_items:
                if item.id == self.id:
                    return
            all_items.append(self)

    def start_inventory_items():
        #   Flowers
        lily = InventoryItem( 0, "Lily", 99, "Flower", True, 5, 1, 0,"Lilium. Tall, majestic and strikingly-shaped")
        rose = InventoryItem(1, "Rose", 99, "Flower", True,  8, 2, 1, "Rosa. Perhaps the most famous flower on the list")
        tulip = InventoryItem(2, "Tulip", 99, "Flower", True, 5, 1, 0, "Tulipa. Closely related to the lily and with a long history of cultivation.")
        carnation = InventoryItem(3, "Carnation", 99, "Flower", True, 12, 3, 2, "Scientific Name: Dianthus.")
        freesia = InventoryItem(4, "Freesia", 99, "Flower", True, 8, 2, 1, "What we call freesias are actually cultivated hybrids.")
        sunflower = InventoryItem(6, "Sunflower", 99, "Flower", True, 8, 2, 1, "Known for its bright and cheery bloom.")
        uncommon_orchid = InventoryItem(7, "Ground Orchid", 99, "Flower", True, 28,  7, 3, "Known for its bright and cheery bloom.")
        rare_orchid = InventoryItem(8, "Z Orchid", 99, "Flower", True, 70, 21, 4,"known for its bright and cheery bloom a rare version or an orchid that can only be found in magic places.")
        blood_rose = InventoryItem(9, "Blood Rose", 99, "Flower", False, 350, 100, 5,"A Very rare rose when the seed is \"watered\" by the blood of a magic creature")
    #   Herbs
        test_herb = InventoryItem(50, "Ghost Herb", 99, "Herb", True, 150, 100, 4,"A Rare herb used to make some potions by wizards")
        # test_herb = InventoryItem(50, "hu", 99, "Herb", True, 150, 100, 4,"test herb")
    #   Potions
        mana_potion = InventoryItem(150, "Lust potion", 5, "Potion", False, 150, 100, 5,"Recovers Mana of the user")
        lust_potion = InventoryItem(151, "Mana potion", 5, "Potion", False, 150, 100, 5,"You may use this potion on special situations")
        healing_potion = InventoryItem(152, "Healing potion", 5, "Potion", False, 150, 100, 5,"Recovers Mana of the user")




    start_inventory_items()

    class ItemReference(object):
        def __init__(self, id, quantity):
            self.id = id
            self.quantity = quantity

        def add_quantity(self, this_quantity):
            self.quantity += this_quantity

        def remove_quantity(self, this_quantity):
            if self.quantity > 0:
                self.quantity -= this_quantity

        def get_item(self):
            for item in all_items:
                if item.id == self.id:
                    return item

        def __del__(self):
            del self
            return
