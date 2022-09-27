__version__ = "0.0.1"
__release__ = "Beta"
__author__ = 'Abhay Patel'
__email__ = 'abhaypgit@gmail.com'  
__status__ = 'Development'
__design_choice__ = 'Simple nodes composed within a linkedlist class'
__improvements__ = 'Please check README.md; for next verison improvements'

import copy
import tags

class Node: 
            
    def __init__(self,data: __builtins__ ) -> None:
        '''Constructor for a node in a linked list'''
        if type(data).__class__.__module__ != 'builtins':
            print(f'Node {data} is of {type(data)},', 'Data within a node must be part of builtins types (SEE: https://docs.python.org/3/library/stdtypes.html)')
            return 
        self.data = data
        self.next = None

    def __repr__(self, data: __builtins__) -> str:
        return 'fNode({self.data})'

class LinkedList:
   
    def __init__(self,*nodes) -> None :
        '''Linked list constructor'''
        self.node = Node(None) # For composition
        
        if type(nodes[0]) == type(self.node):
            try:
                self.__firstnode = nodes[0]
            except:
                print('At least one node is required!')
                return 
        else:
            print(f'Node must be of {type(self.node)}, Not: {type(nodes[0])}!') 
            return
        
        i = 0
        while i + 1 < len(nodes):
                if type(nodes[i + 1]) == type(self.node): 
                    nodes[i].next = nodes[i + 1]
                else:
                    print(f'Node {i + 2} must be of {type(self.node)}, Not: {type(nodes[i + 1])}!') 
                    return

                i += 1

    def __validating_input_parameters(func) -> tags.Function:
        '''Validates method patameters '''
        def __wrapper_function(*args,**kwargs):

            if func.__name__ in [ '__init__' , 'insertEnd','insertStart']:
                pass
            else:
                try:
                    index = args[1]
                except:
                    print(f'Index must be a positive integer, please check your input parameter!')
                    return
                
                if type(index) != type(1):
                    print(f'Node postion must be of type <class \'int\'>, Not: {type(index)}!')
                    return
                elif index <= 0:
                    print(f'Node position must be a integer greater than 0, Not: {index}!')
                    return

            def insertionChecks(data: __builtins__) -> bool:
                if type(data).__class__.__module__ != 'builtins':
                        print(f'Node {data} is of {type(data)},', 
                                'Data within a node must be part of builtins types (SEE: https://docs.python.org/3/library/stdtypes.html)')
                        return True
                return False
            
            if func.__name__ in [ 'insertEnd','insertStart' ] :
                try:
                    if insertionChecks(args[1]):
                        return
                except:
                    print('Node data is empty most likely!')
                    return
                
            match func.__name__:
                case 'insert':
                        if insertionChecks(args[2]):
                            return
                        else: 
                            print('Node data is empty most likely!')
                            return
                case 'access':
                    try:
                        if len(kwargs) > 1:
                            print('Access parameter only accepts one key word argument \'prettify\'!' )
                            return
                        elif len(kwargs) == 1 and 'prettify' in kwargs:
                            to_prettify = kwargs['prettify']
                        else:
                            to_prettify = args[2]

                        if not((to_prettify == True or to_prettify == False) and type(to_prettify) is bool):
                            print(f"Second argument must be a boolean for access method not: {to_prettify},",
                                    "Note: truthy and falsy values aren't accepted")
                            return
                    except:
                        pass

            return func(*args, **kwargs)
        return __wrapper_function

    @__validating_input_parameters
    def access(self, index: int,prettify: bool = False) -> __builtins__:
        ''' Access's a node in a linked list'''
        node = self.__firstnode
        
        for counter in range(1,index):

            if counter == index:
                break

            node = node.next
            if node is None:
                break

        if node is None:
            print(f'Node position is too large, number of nodes: {len(self)}; Node {index} not found!')
            return
        if prettify != False:
            return f'[{node.data}|{hex(id(node.next))}]'
        return node.data

    @__validating_input_parameters
    def insert(self,index: int,data: __builtins__) -> str:
        '''Insert's a node in the linked list'''
        nodePointedTo = self.__firstnode
        toInsertNode = Node(data)
        beforeInsertPointedTo = self.__firstnode
        
        for counter in range(1,index + 1):
            if counter == index:
                toInsertNode.next = nodePointedTo
                break
            elif nodePointedTo is None:
                break
            nodePointedTo = nodePointedTo.next 
       
        if index > counter:
            print(f'Node position is too large, number of nodes: {len(self)}; Max number insertion can occur at node {len(self) + 1}')
            return
       
        for counter in range(1,index):
            if counter + 1 == index:
                beforeInsertPointedTo.next = toInsertNode
                break
            beforeInsertPointedTo = beforeInsertPointedTo.next
        
        return f'Node inserted at position: {index}'
    
    @__validating_input_parameters
    def insertEnd(self,data: __builtins__) -> str:
        '''Insert Node at the end of the linked list'''
        nodePointedTo = self.__firstnode
        toInsertNode = Node(data)

        while nodePointedTo.next is not None:
            nodePointedTo = nodePointedTo.next 
        nodePointedTo.next = toInsertNode
        return 'Node inserted at the end!'
         
    @__validating_input_parameters
    def delete(self,index: int) -> str:
        ''' Delete's a node in a the linked list'''
        if index > len(self):
            print(f'Deletion can\'t occur; As node {index} is out of range, linked list length: {len(self)}')
            return 

        if index == 1: 
            newFirstNode = self.__firstnode.next
            del self.__firstnode
            self.__firstnode = newFirstNode
        elif index == len(self):
            node = self.__firstnode
            for counter in range(1,len(self)):
                if counter == len(self) - 1:
                    lastNode = node.next
                    del lastNode
                    node.next = None
                node = node.next
        else:
            node = self.__firstnode
            for counter in range(1,len(self)):
                if counter + 1 == index: 
                    toDeleteNode = node.next
                    node.next = node.next.next
                    del toDeleteNode 
                node = node.next
        return f'Node deleted at position {index}!'
    
    @__validating_input_parameters
    def insertStart(self,data: __builtins__) -> str:
        '''Insert Node at the start'''
        firstnode = Node(data) 
        firstnode.next = self.__firstnode  
        self.__firstnode = firstnode  
        return 'First node inserted!'
    
    def deleteEnd(self) -> str:
        '''Delete the last node'''
        node = self.__firstnode
        if len(self) == 2:
            node.next = None
        else:
            while node.next.next != None:
                node = node.next 
            node.next = None       
        return 'Last node deleted!'

    def deepcopy(self) -> tags.LinkedList: 
        '''Returns a deep copy of the object'''
        selfDeepCopy = copy.deepcopy(self)
        return selfDeepCopy

    def display(self) -> str:
        '''Method that calls __str__, returns string representation'''
        return self.__str__()

    def len(self) -> int:
        '''Method that calls __len__, returns length of linked list'''
        return self.__len__()

    def reverse(self) -> str:
        '''Reverse's the linked list'''
        length = len(self) - 2
        length2 = length
        while length >= 0:
            node = self.__firstnode 
            for x in range(length):
                if x + 1 == length:
                    node.next.next = node
                    if x + 1 == length2:
                        new_node = node.next
                node = node.next
            length -= 1
        node = self.__firstnode
        node.next = None
        self.__firstnode = new_node
        return 'Linked List has been reversed'
        
    def __len__(self) -> int:
        '''Gives length of linked list'''
        node = self.__firstnode
        linkedListLen = 1

        while node is not None:
            node = node.next
            linkedListLen += 1
        return linkedListLen 
    
    def __str__(self) -> str:
        '''String reperesentation of node'''
        node = self.__firstnode
        out = ''
        
        while node.next is not None:
            out += f'[{str(node.data)}|{hex(id(node.next))}] -> '
            node = node.next
        out += f'[{str(node.data)}|{str(node.next)}]'
        return out

    def __repr__(self) -> str:
        '''Object representation'''
        node = self.__firstnode
        out = ''

        while node.next is not None: 
            out += f"Node({node.data}),"
            node = node.next 
        out += f"Node({node.data})"
        return f"LinkedList({out})"

