class LinkedList {

    LinkedNode head;
    LinkedNode tail;
    int size;

    private class LinkedNode {
        int value;
        LinkedNode next;

        public LinkedNode(int value){
            this.value = value;
            this.next = null;
        }
    }

    public LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public int get(int index) {
        if(index >= size){
            return -1;
        }
        int curIdx = 0;
        LinkedNode travNode = head;
        while (curIdx != index){
            travNode = travNode.next;
            curIdx++;
        }
        return travNode.value;
    }

    public void insertHead(int val) {
        LinkedNode newNode = new LinkedNode(val);
        newNode.next = head;
        this.head = newNode;
        if (size == 0){
            this.tail = newNode;
        }
        size++;
    }

    public void insertTail(int val) {
        LinkedNode newNode = new LinkedNode(val);
        if(size == 0){
            this.head = newNode;
            this.tail = newNode;
            size++;
        }
        else{
            this.tail.next = newNode;
            this.tail = this.tail.next;
            size++;
        }
    }

    public boolean remove(int index) {
        if(index >= size){
            return false;
        }
        
        if(index == 0){
            this.head = this.head.next;
            size--;
            return true;   
        }

        LinkedNode travNode = head;
        int curIdx = 0;
        
        while(curIdx + 1 != index){
            travNode = travNode.next;
            curIdx++;
        }

        if (travNode.next == this.tail){
            this.tail = travNode;
            size--;
            return true;
        }

        else{
            travNode.next = travNode.next.next;
            size--;
            return true;
        }
        
    }


    public ArrayList<Integer> getValues() {
        ArrayList<Integer> listVals = new ArrayList<>();

        LinkedNode travNode = this.head;

        while(travNode != null){
            listVals.add(travNode.value);
            travNode = travNode.next;
        }

        return listVals;
    }

}
