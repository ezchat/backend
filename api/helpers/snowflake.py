from time import time as time_ms


# This class is used by us to generate "Snowflakes"
# These aren't technically Twitter/Discord Snowflakes, since they're 40 bit.
class Snowflake:
    def __init__(self):
        self.last_epoch = 0
        self.increment = 0

    def generate_snowflake(self):
        time = int(time_ms())
        if self.last_epoch == time:
            self.increment += 1
        else:
            self.last_epoch = time
            self.increment = 0
        # Generate a Snowflake computing 33 bit epoch and 7 bits of increment.
        binary_epoch = bin(time)
        binary_increment = bin(self.increment)[2:]
        extra_bits = ((7 - len(binary_increment)) * '0')
        return str(int(binary_epoch + binary_increment + extra_bits, 2))
