#include <iostream>

class DynamicArray {
private:
    int *arr;
    int capacity;
    int size;

public:
    DynamicArray() : arr(nullptr), capacity(0), size(0) {}

    ~DynamicArray() {
        if (arr != nullptr) {
            delete[] arr;
        }
    }

    void push_back(int value) {
        if (size >= capacity) {
            int newCapacity = (capacity == 0) ? 1 : capacity * 2;
            int *newArr = new int[newCapacity];
            for (int i = 0; i < size; ++i) {
                newArr[i] = arr[i];
            }
            delete[] arr;
            arr = newArr;
            capacity = newCapacity;
        }
        arr[size++] = value;
    }

    int at(int index) {
        if (index < 0 || index >= size) {
            std::cerr << "Index out of range\n";
            return -1; // Not a good practice, but for simplicity
        }
        return arr[index];
    }

    int getSize() const {
        return size;
    }

    int getCapacity() const {
        return capacity;
    }
};

int main() {
    DynamicArray dynArr;
    for (int i = 0; i < 10; ++i) {
        dynArr.push_back(i * 10);
    }

    std::cout << "Size of the array: " << dynArr.getSize() << std::endl;
    std::cout << "Capacity of the array: " << dynArr.getCapacity() << std::endl;

    for (int i = 0; i < dynArr.getSize(); ++i) {
        std::cout << "Element at index " << i << ": " << dynArr.at(i) << std::endl;
    }

    return 0;
}
Output:

Size of the array: 10
Capacity of the array: 16
Element at index 0: 0
Element at index 1: 10
Element at index 2: 20
Element at index 3: 30
Element at index 4: 40
Element at index 5: 50
Element at index 6: 60
Element at index 7: 70
Element at index 8: 80
Element at index 9: 90


