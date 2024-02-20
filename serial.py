class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """initializes and sets attributes original number and
            number to increment """
        self.original_num = start
        self.next = start

    def __repr__(self):
        return f"""<SerialGenerator original_number= {self.original_num},
        next_num= {self.next}> """

    def generate(self):
        """method to increment number by one and return next number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """method to reset number to original number"""
        self.next = self.original_num
