class TreeNode {
    constructor(value = 0, left = null, right = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

function preorderTraversalWithStack(root) {
    let stack = [root];
    let result = [];
    while (stack.length > 0) {
        let node = stack.pop();
        if (node) result.push(node.value);
        if (node.right) stack.push(node.right);
        if (node.left) stack.push(node.left);
    }
    return result;
}

function preorderTraversal(root) {
    let result = [];
    function dfs(node) {
        if (node) {
            result.push(node.value);
            if (node.left) dfs(node.left);
            if (node.right) dfs(node.right);
        }
    }
    dfs(root);
    return result;
}

// Create the binary tree
let root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(7);

console.log(preorderTraversalWithStack(root));
console.log(preorderTraversal(root));
/*
           1
          / \
         2   3
        / \ / \
       4  5 6  7

*/
