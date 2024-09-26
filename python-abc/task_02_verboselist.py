#!/usr/bin/env python3
class VerboseList(list):
    # Overriding the append method
    def append(self, item):
        super().append(item)  # Call the original append method
        print(f"Added {item} to the list.")

    # Overriding the extend method
    def extend(self, iterable):
        super().extend(iterable)  # Call the original extend method
        print(f"Extended the list with {len(iterable)} items.")

    # Overriding the remove method
    def remove(self, item):
        if item in self:
            print(f"Removed {item} from the list.")  # Print before removal
            super().remove(item)  # Call the original remove method
        else:
            print(f"{item} not found in the list.")

    # Overriding the pop method
    def pop(self, index=None):
        # If index is provided, pop that specific item; else, pop the last one
        if index is None:
            popped_item = super().pop()
            print(f"Popped {popped_item} from the list.")
            return popped_item
        else:
            popped_item = super().pop(index)
            print(f"Popped {popped_item} from index {index} in the list.")
            return popped_item
