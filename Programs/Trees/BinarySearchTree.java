class Node { 
	
	int data; 
	Node left, right; 
	
	Node(int d) { 
		data = d; 
		left = right = null; 
	} 
} 

class BinarySearchTree { 
	
	static Node root; 

	Node sortedArrayToBST(int arr[], int start, int end) { 

		if (start > end) { 
			return null; 
		} 

		int mid = (start + end) / 2; 
		Node node = new Node(arr[mid]); 
		node.left = sortedArrayToBST(arr, start, mid - 1); 
		node.right = sortedArrayToBST(arr, mid + 1, end); 		
		return node; 
	} 

	void preOrder(Node node) { 
		if (node == null) { 
			return; 
		} 
		System.out.print(node.data + " "); 
		preOrder(node.left); 
		preOrder(node.right); 
	} 
	
	public static void main(String[] args) { 
		BinarySearchTreeTree tree = new BinarySearchTree(); 
		int arr[] = new int[]{1, 2, 3, 4, 5, 6, 7}; 
		int n = arr.length; 
		root = tree.sortedArrayToBST(arr, 0, n - 1); 
		System.out.println("Preorder traversal"); 
		tree.preOrder(root); 
	} 
} 
 
