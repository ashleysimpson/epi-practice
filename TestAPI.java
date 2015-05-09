import java.util.ArrayList;

public class TestAPI {

	public static void main(String[] args) {

		// setting the lockstate
		Node locked =  new Node(LockState.LOCKED);
		Node unlocked = new Node(LockState.UNLOCKED);

		Node[] newTree = {new Node(LockState.LOCKED), new Node(LockState.UNLOCKED), new Node(LockState.UNLOCKED)};
		LockAPI test = new LockAPI(newTree);

		System.out.println("Test isLocked():");
		if (test.isLocked(0)) {
			System.out.println("PASS!");
		} else {
			System.out.println("FAIL!");
		}
		if (!test.isLocked(1)) {
			System.out.println("PASS!");
		} else {
			System.out.println("FAIL!");
		}
		if (!test.isLocked(1)) {
			System.out.println("PASS!");
		} else {
			System.out.println("FAIL!");
		}

		System.out.println("Test unLock():");
		test.unLock(0);	
		if (!test.isLocked(0)) {
			System.out.println("PASS!");
		} else {
			System.out.println("FAIL!");
		}

		System.out.println("Test lock():");
		Node[] newTree1 = {locked, unlocked, unlocked, unlocked, unlocked};
		LockAPI test1 = new LockAPI(newTree1);
		Node[] newTree2 = {unlocked, unlocked, unlocked, unlocked, locked};
		LockAPI test2 = new LockAPI(newTree2);
		Node[] newTree3 = {unlocked, unlocked, unlocked, unlocked, unlocked};
		LockAPI test3 = new LockAPI(newTree3);
		test1.lock(4);
		test2.lock(1);
		test3.lock(1);
		test1.lock(4);
		test3.lock(1);
		test3.unLock(1);
		test3.lock(1);
	}
}

enum LockState { 
	LOCKED, UNLOCKED, UNUSED
}

// the lock API
class LockAPI {
	ArrayList<Node> binaryTree = new ArrayList<Node>();

	public LockAPI(Node[] tree) {

		for (int i = 0; i < tree.length; i++) {
			binaryTree.add(tree[i]);
		}

	}

	public boolean isLocked(int index) {
		switch (binaryTree.get(index).getLockState()) {
			case LOCKED:
				return true;
			case UNLOCKED:
				return false;
			default:
				return false;
		}
	}

	public void lock(int index) {
		if (!(isAParentLocked(index) || isAChildLocked(index))) {
			binaryTree.get(index).setLockState(LockState.LOCKED);
			System.out.println("Locked!");
		} else {
			System.out.println("Cannot Lock!");
		}
	}

	public void unLock(int index) {
		binaryTree.get(index).setLockState(LockState.UNLOCKED);
	}

	public void addNode(Node newNode) {
		binaryTree.add(newNode);
	}

	private boolean isAParentLocked(int index) {
		// if at first node, last check
		if (index == 0) {
			return isLocked(0);
		}

		// if locked then return true, else recursively check next parent
		if (isLocked(index)) {
			return true;
		} else {
			return isAParentLocked((int)Math.ceil(index/2.0)-1);
		}
	}

	private boolean isAChildLocked(int index) {
		// if passed the limit return false
		if (index >= binaryTree.size()) {
			return false;
		}

		// if detected lock then return true, else check deeper
		if (isLocked(index)) {
			return true;
		} else {
			boolean leftChild = isAChildLocked(2*index + 1);
			boolean rightChild = isAChildLocked(2*index + 2);
			return (leftChild || rightChild);
		}

	}
}

// simple node class
class Node {
	LockState state;

	public Node(LockState state) {
		this.state = state;
	}

	public void setLockState(LockState state) {
		this.state = state;
	}

	public LockState getLockState() {
		return this.state;
	}
}