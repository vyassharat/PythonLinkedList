"""
Author: Sharat Vyas
Date: 12/11/2019
Based of off skeleton implementation provided in ITCS 6114.
This class creates a single-way linked list. This mean each linked list
holds a reference to its child. The list is made of LNodes where the LNode
implementation was provided. Each LNode will
contain a data-value and will hold a reference to it's child.

"""
from LNode import LNode


class LList:
    def __init__(self):  # O(1)
        """ Initializes empty list and set size to 0"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):  # O(1)
        """
        Returns LList's size
        :return: LList's size
        """
        """ return the size"""
        return self._size

    def getItemAtIndex(self, index):
        """

        :param index: The index you want to get data from
        :return: Will return the LNode at the specified index
        """
        """ Allows you to get the node at a specific index of the list"""
        """ Handles cases where you try to index somewhere you shouldn't"""
        if index < 0 or index > self._size:
            raise IndexError

        """
        if you're indexing the head, return 
        head otherwise iterate thru list
        """
        currentNode = self._head
        if index == 0:
            return self._head
        else:
            for i in range(0, index + 1):
                if i == index:
                    return currentNode
                else:
                    currentNode = currentNode.get_next()

    def append(self, item):  # ALWAYS O(1) (not amortized like built-in)
        """
        This will add an item to the end of the list
        :param item: The value of the item you want appended to end of list
        :return: N/A
        """
        """ Insert item at end of list as new node. """
        """Create a new node item"""
        myNode = LNode(item)

        """ 
        if there isn't a head make it the head otherwise
        append to the end of the list
        """
        if self._head is None or self._size == 0:
            self._head = myNode
            self._tail = myNode
            self._size = 1
        else:
            self._tail.set_next(myNode)
            self._tail = myNode
            self._size += 1

    def insert(self, index, item):  # O(index)
        """
        This will insert an item at a specified index
        :param index: The index at which you want the item inserted
        :param item: The value of the item to be inserted
        :return: N/A but error can be raised
        """
        """Insert item at position index. """
        """
        This will insert an item at the specified index
        It will shift the current element at that index right one
        """
        newNode = LNode(item)

        """ 
        Handles cases where you try to insert 
        somewhere you shouldn't
        """
        if (index > 0 and index >= self._size) or index < 0:
            raise IndexError

        """
        if indexing anywhere but head we need to adjust the 
        index's parent and child so we request these otherwise to insert 
        at head we just need to adjust the
        current head and its child if it exists
        """
        if index > 0:
            nodeToShift = self.getItemAtIndex(index)
            nodeToShiftsParent = self.getItemAtIndex(index - 1)
            nodeToShiftsParent.set_next(newNode)
            newNode.set_next(nodeToShift)
            self._size += 1
        elif index == 0:
            if self._size == 0:
                self.append(item)
            else:
                currentHead = self._head
                self._head = newNode
                newNode.set_next(currentHead)
                self._size += 1


    def __getitem__(self, index):  # O(index) - worse than built in!
        """
        Allows you to use native operators to get value of item at index
        :param index: The index of the item you're interested in
        :return: The value of the node at the specified index
        """
        """ 
         This calls the getItemAtIndex method and gets
         the underlying node's data
         """
        return self.getItemAtIndex(index).get_data()



    def __setitem__(self, index, item):  # O(index) - worse than built in!
        """
        Allows you to use python array operators to set value of item in
        index
        :param index: The index of the item whose value you want updated
        :param item: The new value of the item at specified index
        :return: N/A but error can be raised
        """
        """
        This will insert the item at the index and remove the element that
        was previously occupying the specified index
        """
        self.insert(index, item)
        self.pop(index + 1)

        #raise NotImplementedError

    def pop(self, index):  # O(index) - faster at beginning of list
        """
        Will remove an item at index passed as param
        :param index: The index of the item we want removed
        :return: No specific return but error can be raised
        """

        """ Remove the node at index given in the parameter """

        """ Handles cases where you try to pop somewhere you shouldn't"""
        if index == self._size or index < 0:
            raise IndexError

        """
        First we handle cases where we try to pop the head or tail since 
        those require extra precautions. If we're not popping the head/tail
        we can proceed as planned. We basically just get the parent of the 
        item at the index we specified and point it to the item of 
        interest's child
        """
        if self._size-1 == index:
            self._tail = self.getItemAtIndex(index -1)
            self._size -= 1
            return
        elif index == 0:
            self._head = self._head.get_next()
            self._size -= 1
            return
        else:
            currentItemAtIndex = self.getItemAtIndex(index)
            parentItem = self.getItemAtIndex(index - 1)
            if index == self._size:
                self._tail = parentItem
            parentItem.set_next(currentItemAtIndex.get_next())
            self._size -= 1
            return

        raise ValueError
        # raise NotImplementedError

    def remove(self, item):  # O(n) - same as built in list
        """
        Will remove the item passed
        :param item: The node we want to remove
        :return: Nothing is returned but an error is rasied if the
        item DNE
        """

        """ Removes the first node containing the data item """

        """ First check if the element we're trying to remove exists"""
        if not self.__contains__(item):
            raise ValueError

        """
        handle special case where we're removing the head
        if we're not removing the head, then we will do a similar approach
        where we will get the item's parent and child and will point 
        the item's parent's to the item's child. 
        As a result the item is dropped from the list
        """
        if self._head.get_data() == item:
            if self._head.get_next() is not None:
                self._head = self._head.get_next()
                self._size -= 1
                return
            else:
                self._head = None
                self._size = 0
                self._tail = None
                return
        else:
            for i in range(1, self._size):
                parent = self.getItemAtIndex(i - 1)
                currentNode = self.getItemAtIndex(i)
                if currentNode.get_data() == item:

                    if i == self._size -1:
                        self._tail = parent

                    parent.set_next(currentNode.get_next())
                    self._size -= 1
                    break

    def __contains__(self, item):  # O(n) - same as built in
        """

        :param item: The item we want to check if the list contains
        :return: T/F depending on if the list has the item or not
        """
        """ Support notation item in LList """
        """ 
        Iterate thru the list until you find the 
        first occurrence of the item. If you get to the end
        and can't find it, throw an error
        """
        currentNode = self._head
        for i in range(0, self._size):
            if currentNode.get_data() == item:
                return True
                break
            else:
                currentNode = currentNode.get_next()

        return False


    """ Clears the list """
    def clear(self):  # O(1)
        self._head = None
        self._tail = None
        self._size = 0



    def index(self, item):# O(n)
        """

        :param item: The item whose index we want
        :return: The index of the item of interest
        """
        """ check if the item even exists first"""
        if not self.__contains__(item):
            raise ValueError

        """
        Allows you to get the index in the list of a specific item.
        First will check if it's the head, if it's not
        then will iterate thru the list keep tracking of what index
        it's currently on and if there's a match, that current index
        is returned
        """
        currentNode = self._head
        if currentNode.get_data() == item:
            return 0
        else:
            for i in range(1, self._size):
                currentNode = currentNode.get_next()
                if currentNode.get_data() == item:
                    return i

        return ValueError

    def __str__(self):  # O(n^2), n = len of list
        # Note: we could change the body of this function get
        # it down to O(n)
        # First, check for empty list
        if self._head == None:
            return '[ ]'

        beginning = '['
        end = ']'
        middle = ''
        current = self._head
        middle += str(current.get_data())
        while current != self._tail:
            current = current.get_next()
            middle += ', ' + str(current.get_data())
        return beginning + middle + end
