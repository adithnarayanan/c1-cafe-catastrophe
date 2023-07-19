from lib.customer import Customer

class CustomerHandler:
    def __init__(self):
        self.chance_of_spawn = 0.3

        self.lines = [[],[],[],[]]

    #call every 5 seconds in game
    def spawn_cust(self):
        smallest_line = min(self.lines, key=len)
        smallest_line.append(Customer())

    #call every 1 second in game
    def decrement_time(self):
        num_removes = 0
        for line in self.lines:
            should_pop = False
            for cust in line:
                cust.max_wait_time -= 1
                if cust.max_wait_time == 0:
                    should_pop = True
            if should_pop:
                line.pop(0)
                num_removes = num_removes + 1
        return num_removes

    def drawCustomers(self, screen, interactionXPoints, Y):
        for i in range(4):
            if len(self.lines[i]) > 0:
                self.lines[i][0].draw(screen, interactionXPoints[i], Y)
    
    #call whenever player interacts with a line

    def pop_customer_from_line(self, i):
        return self.lines[i].pop(0)

    def pop_customer_from_line_1(self):
        return self.lines[0].pop(0)

    def pop_customer_from_line_2(self):
        return self.lines[1].pop(0)

    def pop_customer_from_line_3(self):
        return self.lines[2].pop(0)

    def pop_customer_from_line_4(self):
        return self.lines[3].pop(0)
