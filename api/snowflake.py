from time import time_ns


class Snowflake:
    def __init__(self):
        self.last_epoch = 0
        self.increment = 0

    def generate_snowflake(self):
        time = time_ns() / 1000
        if self.last_epoch == time:
            self.increment += 1
        else:
            self.last_epoch = time
            self.increment = 0
        # Generate a Snowflake computing 51 bit epoch and 7 bits of increment.
        binary_epoch = bin(time)
        binary_increment = bin(self.increment)[2:]
        extra_bits = ((7 - len(binary_increment)) * '0')
        return str(int(binary_epoch + binary_increment + extra_bits, 2))
