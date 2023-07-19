import customer

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
        for line in lines:
            should_pop = False
            for cust in line:
                cust.max_wait_time -= 1
                if cust.max_wait_time == 0:
                    should_pop = True
            if should_pop:
                line.pop(0)
    
    #call whenever player interacts with a line
    def pop_customer_from_line_1(self):
        return lines[0].pop(0)

    def pop_customer_from_line_2(self):
        return lines[1].pop(0)

    def pop_customer_from_line_3(self):
        return lines[2].pop(0)

    def pop_customer_from_line_4(self):
        return lines[3].pop(0)
