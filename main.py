import pandas as pd


def get_address_to_write(tag, slot, offset):
    comp = [tag, slot, offset]
    comp = [str(hex(i))[2:] for i in comp]
    address_to_write = "".join(comp)
    address_to_write = int(address_to_write, 16)
    return address_to_write


def initialize_memory(size=0x7FF):
    memory = [i % 0x100 for i in range(size + 1)]
    return memory


def get_offset(address):
    return address & 0b000000001111


def get_slot(address):
    return (address & 0b000011110000) >> 4


def get_tag(address):
    return (address & 0b111100000000) >> 8


def get_tag_slot_offset(address):
    offset = get_offset(address)
    slot = get_slot(address)
    tag = get_tag(address)
    return tag, slot, offset


class Cache:
    # Direct Mapped Cache
    # Block size is 16 bytes
    # 16 slots in the cache
    def __init__(self, number_of_slots=16, main_memory=None):
        if main_memory is None:
            self.main_memory = initialize_memory()

        self.number_of_slots = number_of_slots
        self.cache_slots = [Record(slot=i, valid=0, tag=0, block_data=Block()) for i in range(0, number_of_slots)]
        print("Cache initialized")

    def get_record_by_slot(self, slot):
        for record in self.cache_slots:
            if record.slot == slot:
                return record
        return None

    def get_block_from_memory(self, address):
        offset = get_offset(address)
        block_starting_address = address - offset
        # Block size is 16 bytes so we add 15 to the starting address to get the end address and add 1 to include it
        block_end_address = block_starting_address + 15 + 1
        block = self.main_memory[block_starting_address:block_end_address]
        return block

    def read(self, address):
        tag, slot, offset = get_tag_slot_offset(address)

        record_in_cache = self.get_record_by_slot(slot)
        cache_hit = (record_in_cache.tag == tag and record_in_cache.valid == 1)
        if cache_hit:
            print(f"Read {hex(address)} -> tag={hex(tag)}, slot={hex(slot)}, offset={hex(offset)} (Cache hit)")
            print("Data: ", hex(record_in_cache.block_data.block[offset]))
        else:
            print(f"Read {hex(address)} -> tag={hex(tag)}, slot={hex(slot)}, offset={hex(offset)} (Cache miss)")

            if record_in_cache.dirty:
                print("Dirty bit found in slot: ", hex(slot))
                address_to_write_old_block = get_address_to_write(record_in_cache.tag, slot, offset)
                self.write_block_to_memory(address_to_write_old_block, record_in_cache.block_data.block)
                record_in_cache.dirty = 0

            print(f"Retrieving block starting at {hex(address - offset)} from memory...")
            block_to_add_to_cache = Block(block=self.get_block_from_memory(address))
            record_in_cache.block_data = block_to_add_to_cache
            record_in_cache.tag = tag
            record_in_cache.valid = 1
            print("Data: ", hex(record_in_cache.block_data.block[offset]))

    def write_block_to_memory(self, address, data):
        offset = get_offset(address)
        block_starting_address = address - offset
        block_end_address = block_starting_address + 16
        print(f"Writing block {hex(block_starting_address)} to memory...")
        self.main_memory[block_starting_address:block_end_address] = data

    def write(self, address, data):
        tag, slot, offset = get_tag_slot_offset(address)
        data_hex_str = hex(data)[2:]
        record = self.get_record_by_slot(slot)

        print(f"Write {hex(data)} to {hex(address)} -> tag: ", hex(tag), "slot: ", hex(slot), "offset: ", hex(offset))

        def add_block_to_cache_record_from_memory(record, block_address):
            block_to_add_to_cache = Block(block=self.get_block_from_memory(block_address))
            record.block_data = block_to_add_to_cache
            record.tag = tag
            record.valid = 1
            record.block_data.block[offset] = data
            record.dirty = 1
            print(f"Data: {data_hex_str} written to cache")

        if record.tag == tag and record.valid == 1:
            print("Cache hit")
            record.block_data.block[offset] = data
            record.dirty = 1
            print(f"Data: {data_hex_str} written to cache")

        elif record.tag != tag and record.dirty == 1:
            print("Cache miss")
            print("Dirty bit found in slot: ", hex(slot))
            print("Writing old record to memory...")

            # Write the old record to memory
            old_block = record.block_data.block
            address_to_write_old_block = get_address_to_write(record.tag, slot, offset)
            self.write_block_to_memory(address_to_write_old_block, old_block)
            print("Old record written to memory")

            record.dirty = 0
            print("Now retrieving block starting at ", hex(address - offset), " from memory...")
            add_block_to_cache_record_from_memory(record, address)

        else:
            print("Cache miss")
            print("Retrieving block starting at ", hex(address - offset), " from memory...")
            record = self.get_record_by_slot(slot)
            # Now retrieve the required block from memory
            add_block_to_cache_record_from_memory(record, address)

    def display(self):
        df = pd.DataFrame([vars(i) for i in self.cache_slots])
        column_names = ["slot", "valid", "tag", "dirty", " ", "block_data"]
        # Add a column with no data between tag and data
        df[" "] = ""

        df = df[column_names]

        df["slot"] = df["slot"].apply(hex)
        df["slot"] = df["slot"].apply(lambda x: x[2:])
        df["tag"] = df["tag"].apply(hex)
        df["tag"] = df["tag"].apply(lambda x: x[2:])

        print(df)


class Record:
    def __init__(self, slot, valid, tag, block_data):
        self.block_data = block_data
        self.slot = slot
        self.tag = tag
        self.valid = valid
        self.dirty = 0


class Block:
    def __init__(self, size=16, block=None):
        self.size = size
        if block is None:
            self.block = []
            for _ in range(0, size):
                self.block.append(0)
        else:
            self.block = block

    def __str__(self):
        string = ""
        for i in self.block:
            hex_repr = hex(i)[2:]
            if len(hex_repr) == 1:
                string += hex_repr + "  "
            else:
                string += hex_repr + " "
        return string


def user_interface(cache):
    while True:
        print("To interact with the cache please select an action (R)ead, (W)rite, (D)isplay ->")
        action = input().lower().strip()
        match action:
            case "r":
                user_read(cache)
            case "w":
                user_write(cache)
            case "d":
                user_display(cache)
            case _:
                print("Invalid input!")


def user_read(cache):
    print("Read selected.")
    print("What address would you like to read? Please enter in hex")
    print("Max tag is 7, max slot is F, max offset is F")
    address = input()
    address = int(address, 16)
    cache.read(address)


def user_write(cache):
    print("Write selected.")
    print("What address would you like to write to? Please enter in hex")
    print("Max tag is 7, max slot is F, max offset is F")
    address = input()
    address = int(address, 16)
    print("What data would you like to write? Please enter in hex")
    data = input()
    data = int(data, 16)
    cache.write(address, data)


def user_display(cache):
    print("Display selected.")
    cache.display()


def main():
    # cache = Cache()
    # user_interface(cache)
    final_test()


def final_test():
    cache = Cache()
    addresses_to_read = [0x5, 0x6, 0x7, 0x14c, 0x14d, 0x14e, 0x14f, 0x150, 0x151, 0x3A6, 0x4C3]
    for x in addresses_to_read:
        cache.read(address=x)
        cache.display()
        print("\n")

    cache.write(0x14c, 0x99)
    cache.display()
    print("\n")

    cache.write(0x63B, 0x7)
    cache.display()
    print("\n")

    cache.read(0x582)
    cache.display()
    print("\n")

    cache.read(0x348)
    cache.display()
    print("\n")

    cache.read(0x3f)
    cache.display()
    print("\n")

    cache.read(0x14b)
    cache.display()
    print("\n")

    cache.read(0x14c)
    cache.display()
    print("\n")

    cache.read(0x63f)
    cache.display()
    print("\n")

    cache.read(0x83)
    cache.display()
    print("\n")


if __name__ == "__main__":
    # Ensure there is no max width for dataframe
    pd.set_option("display.max_columns", None)
    pd.set_option("display.expand_frame_repr", False)
    pd.set_option('display.width', 1000)

    main()
