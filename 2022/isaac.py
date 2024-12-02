@dataclasses.dataclass
class Node:

    val: Optional[int]
    prev: Optional[Node] = None
    next: Optional[Node] = None

    def __post_init__(self):
        if self.next:
            self.next.prev = self
        if self.prev:
            self.prev.next = self


@dataclasses.dataclass
class LinkedList:

    def __init__(self):
        """Create a double linked list."""
        self.head = Node(None)
        self.tail = Node(None, prev=self.head)
        self.nodes = []

    def seal(self):
        """Convert the list to a circular list."""
        self.first = self.head.next
        self.last = self.tail.prev
        self.first.prev = self.last
        self.last.next = self.first
        self.len = len(self.nodes)

    def add(self, val):
        """Insert a new value at the end of the list."""
        self.nodes.append(Node(val, prev=self.tail.prev, next=self.tail))

    def find_p1(self):
        """Return the 1000th, 2000th, 3000th value after 0."""
        out = []
        cur = self.first
        while cur.val != 0:
            cur = cur.next
        for _ in range(3):
            for i in range(1000):
                cur = cur.next
            out.append(cur.val)
        return out

    def move_after(self, node, insert_after):
        """Move a node from its current location to the postion after insert_after."""
        # Remove the node from the old location and close the gap.
        node.prev.next, node.next.prev = node.next, node.prev
        # Insert between insert_after and insert_after.next
        node.prev, node.next = insert_after, insert_after.next
        node.prev.next, node.next.prev = node, node

    def move(self, node):
        insert_after = node
        movement = node.val
        if movement == 0:
            return
        if movement > 0:
            for _ in range(movement):
                insert_after = insert_after.next
        if movement < 0:
            for _ in range(abs(movement) + 1):
                insert_after = insert_after.prev
        self.move_after(node, insert_after)


class Day20(aoc.Challenge):
    """Day 20: Grove Positioning System."""

    def part1(self, parsed_input: InputType) -> int:
        nodelist = LinkedList()
        for i in parsed_input:
            nodelist.add(i)
        nodelist.seal()

        self.debug(f"Node count: {len(nodelist.nodes)} == {nodelist.len}")
        for node in nodelist.nodes:
            nodelist.move(node)

        out = nodelist.find_p1()
        res = sum(out)
        self.debug(f"{out} => {res}")
        if not self.testing:
            assert res != 1386
            assert res != 2487
            assert res != 4102
            assert res != 6303
            assert res > 6303
        return res


if __name__ == "__main__":
    typer.run(Day20().run)

# vim:expandtab:sw=4:ts=4

