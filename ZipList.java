import java.util.Scanner;

public class ZipList {
	public static void main(String[] args) {

		// allow user to indicate the length of the linked list
		System.out.println("Please indicate length of the list: ");
		Scanner scanner = new Scanner(System.in);
		
		// catch exception when integer not entered
		int listLength = 0;
		try {
			listLength = scanner.nextInt();
		} catch (Exception e) {
			System.out.println("Please enter an integer value!");
			return;
		}

		// setup the LinkedNode
		LinkedNode headNode = new LinkedNode(0);

		LinkedNode node = headNode;
		LinkedNode previousNode = node;

		for (int i = 1; i < listLength; i++) {
			previousNode = node;
			node = new LinkedNode(i);
			previousNode.setPointer(node);
		}

		// test the output
		node = headNode;

		while(node.getPointer() != null) {
			System.out.println(node.getData());
			node = node.getPointer();
		}

		System.out.println(node.getData());
		System.out.println("");

		// zip the linkedlist
		LinkedNode trackedNode = headNode;
		LinkedNode nextNode = node;

		while (trackedNode.getPointer() != null) {
			nextNode = trackedNode.getPointer();
			node = nextNode;

			int counter = 0;

			while (node.getPointer() != null) {
				previousNode = node;
				node = node.getPointer();
				counter++;
			}

			if (counter == 0) {
				break;
			}

			previousNode.setPointer(null);
			nextNode = trackedNode.getPointer();
			trackedNode.setPointer(node);
			node.setPointer(nextNode);

			trackedNode = nextNode;
		}

		// test the output
		node = headNode;

		while(node.getPointer() != null) {
			System.out.println(node.getData());
			node = node.getPointer();
		}

		System.out.println(node.getData());

	}
}

class LinkedNode {
	int data;
	LinkedNode pointer = null;

	public LinkedNode(int nodeData) {
		data = nodeData;
	}

	public void setPointer(LinkedNode pointer) {
		this.pointer = pointer;
	}

	public LinkedNode getPointer() {
		return pointer;
	}

	public void setData(int data) {
		this.data = data;
	}

	public int getData() {
		return this.data;
	}

}