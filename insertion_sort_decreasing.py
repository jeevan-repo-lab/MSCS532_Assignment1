# ==============================================================================
# Insertion Sort Algorithm - Sorting in Monotonically Decreasing Order
# ==============================================================================
  
def insertion_sort(arr):
    """
    Sorts a list of integers in monotonically decreasing order using the Insertion Sort algorithm.
    
    Parameters:
    arr (list): The list of integers to be sorted.

    Returns:
    list: The sorted list in descending (decreasing) order.
    """
    
    # Iterate through the list starting from the second element.
    for i in range(1, len(arr)):
        # Store the current element to be inserted into the sorted portion.
        key = arr[i]
        
        # Initialize the variable j to compare the key with elements in the sorted portion.
        j = i - 1
        
        # Move elements that are smaller than the key one position to the right.
        # This is done to make space for the key in the sorted section.
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  # Shift the element to the right.
            j -= 1  # Move left in the array to compare the next element.
        
        # Place the key in the correct position within the sorted portion of the array.
        arr[j + 1] = key

    # Return the fully sorted array.
    return arr

# Main function to test the Insertion Sort algorithm
if __name__ == "__main__":
    # Test case: A new example array to be sorted in decreasing order.
    arr = [25, 7, 40, 10, 17]
    
    # Display the array before sorting.
    print("Original array:", arr)
    
    # Perform the insertion sort to arrange the elements in descending order.
    sorted_arr = insertion_sort(arr)
    
    # Display the sorted array.
    print("Sorted array in decreasing order:", sorted_arr)

# ==============================================================================
# End of Program
# ==============================================================================
