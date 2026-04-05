class DynamicArray {
    
    private int[] innerDynamicArray;
    private int size;
    private int lastElement;
    private int innerCapacity;


    public DynamicArray(int capacity){
        innerDynamicArray = new int[capacity];
        size = 0;
        lastElement = -1;
        innerCapacity = capacity;
    }

    public int get(int i) {
        return innerDynamicArray[i];
    }

    public void set(int i, int n) {
        innerDynamicArray[i] = n;
    }

    public void pushback(int n) {
        if(lastElement + 1 >= innerCapacity){
            this.resize();
        }
        lastElement++;
        innerDynamicArray[lastElement] = n;
        size++;
    }

    public int popback() {
        int popped = innerDynamicArray[lastElement];
        lastElement--;
        size--;
        return popped;
    }

    private void resize() {
        int[] resizedArray = new int[innerCapacity * 2];
        for(int i = 0; i < innerDynamicArray.length; i++){
            resizedArray[i] = innerDynamicArray[i];
        }
        innerDynamicArray = resizedArray;
        innerCapacity = innerCapacity * 2;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.innerCapacity;
    }
}
