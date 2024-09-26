#!/usr/bin/env python3
class CountedIterator:
    def __init__(self, iterable):
        # Initialize the iterator and counter
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        # Attempt to fetch the next item from the iterator
        try:
            item = next(self.iterator)
            self.count += 1  # Increment counter after successfully fetching an item
            return item
        except StopIteration:
            # If there are no items left, raise StopIteration
            raise StopIteration

    def get_count(self):
        # Return the number of items iterated
        return self.count

# Example usage
if __name__ == "__main__":
    # Create a CountedIterator object using a list
    items = [10, 20, 30, 40]
    counted_iter = CountedIterator(items)

    # Iterate manually using a loop
    try:
        while True:
            print(next(counted_iter))
            print("Count so far:", counted_iter.get_count())
    except StopIteration:
        print("Iteration complete.")

    # Final count of items iterated
    print("Total items iterated:", counted_iter.get_count())
