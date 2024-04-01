python
import random

class Player:
    def init(self):
        self.fish_caught = 0
        self.bait = 10
        self.inventory = {'rod': 1, 'net': 1, 'hook': 5}

    def catch_fish(self):
        if self.bait > 0 and self.inventory['hook'] > 0:
            self.fish_caught += 1
            self.bait -= 1
            self.inventory['hook'] -= 1

    def buy_bait(self, amount):
        self.bait += amount

    def upgrade_gear(self, item):
        if item in self.inventory:
            self.inventory[item] += 1

class Game:
    def init(self):
        self.player = Player()
        self.levels = 10
        self.quests = {
            'Catch 5 fish': False,
            'Buy 10 bait': False,
            'Upgrade gear': False,
            'Catch 10 fish': False,
        }

    def check_quest_completion(self):
        for quest, completed in self.quests.items():
            if not completed:
                if quest == 'Catch 5 fish' and self.player.fish_caught >= 5:
                    self.quests[quest] = True
                    print(f"You completed the quest: {quest}!")
                elif quest == 'Catch 10 fish' and self.player.fish_caught >= 10:
                    self.quests[quest] = True
                    print(f"You completed the quest: {quest}!")
                elif quest == 'Buy 10 bait' and self.player.bait >= 10:
                    self.quests[quest] = True
                    print(f"You completed the quest: {quest}!")
                elif quest == 'Upgrade gear' and sum(self.player.inventory.values()) > 3:
                    self.quests[quest] = True
                    print(f"You completed the quest: {quest}!")

    def start(self):
        for level in range(1, self.levels + 1):
            print(f"\nStartin
g level {level}")
            self.player.catch_fish()
            print(f"You caught a fish! Total fish caught: {self.player.fish_caught}")
            self.check_quest_completion()
            if level % 2 == 0:
                self.player.buy_bait(5)
                print(f"You bought some bait. Total bait: {self.player.bait}")
                self.check_quest_completion()
            if level % 3 == 0:
                self.player.upgrade_gear('hook')
                print(f"You upgraded your gear. Inventory: {self.player.inventory}")
                self.check_quest_completion()

game = Game()
game.start()
