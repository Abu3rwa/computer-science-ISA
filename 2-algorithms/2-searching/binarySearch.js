class Animal {
  constructor(self) {
    self.color = color;
    self.size = size;
    self.eat = eat;
    self.speed = speed;
  }
}

dog = new Animal();
dog.eat = "it does not eat";
print(dog.eat);

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
class BinarySearch {
  constructor() {
    this.root = null;
  }
  insert(value) {
    let newNode = new Node(value);
    if (this.root == null) {
      this.root = newNode;
      return;
    }
    while (true) {
      let temp = this.root;
      if (newNode.value == temp.value) return false;
      if (newNode.value < temp.value) {
        if (temp.left == null) {
          temp.left = newNode;
          return;
        }
        temp = temp.left;
        if (temp.right == null) {
          temp.right = newNode;
          return;
        }
        temp = temp.right;
      }
      return this.root;
    }
  }
}
let binarySearch = new BinarySearch(3);

binarySearch.insert(49);
binarySearch.insert(9);
binarySearch.insert(7);
binarySearch.insert(889);
console.log(binarySearch.root);
