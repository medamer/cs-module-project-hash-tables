class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = MIN_CAPACITY
        self.my_tab = [None] * self.capacity
        self.head = None
        self.counter = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.my_tab)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = float(self.counter / len(self.my_tab))
        return load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        hash = 0xcbf29ce484222325
        byte_arr = key.encode('utf-8')
        for byte in byte_arr:
            hash = hash * 0x00000100000001B3
            hash = hash ^ byte
            hash = hash % 0x10000000000000000
            
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        byte_arr = key.encode('utf-8')
        for byte in byte_arr:
            hash = ((hash * 33) ^ byte) % 0x100000000
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Get the index:
        index = self.hash_index(key)
        # Create a new node:
        new_node = HashTableEntry(key, value)
        # Check the existing node:
        cur = self.my_tab[index]

        if cur:
            prev = None
            while cur:
                # check if the same key:
                if cur.key == key:
                    # Update the value:
                    cur.value = value
                    return
                prev = cur
                cur = cur.next
            
            prev.next = new_node
        else:
            self.my_tab[index] = new_node
            self.counter +=1



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # If the hash table is empty:
        index = self.hash_index(key)
        cur = self.my_tab[index]
        
        if cur:
            prev = None
            while cur:
                if cur.key == key:
                    if prev:
                        prev.next = cur.next
                    else:
                        self.my_tab[index] = cur.next
                prev = cur
                cur = cur.next
                self.counter -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        cur = self.my_tab[index]


        if cur:
            while cur:
                if cur.key == key:
                    return cur.value
                cur = cur.next

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here:
        load = 0.8 #self.get_load_factor
        if load >= 0.7:
            new_buckets = [None] * new_capacity

            for bucket in self.my_tab:
                for entry in bucket:
                    new_bucket = self.djb2(entry.key) % new_capacity
                    entry.next = new_buckets[new_bucket].next
                    new_buckets[new_bucket].next = entry




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
