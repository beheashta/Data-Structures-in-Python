"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2020-02-13"
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while source.is_empty() != True:
        temp = source.remove()
        if temp < key:
            target1.insert(temp)
        else:
            target2.insert(temp)
            
    target1._set_first()
    target2._set_first()
    
    return target1, target2


def pq_split_alt(source):
    """
    -------------------------------------------------------
    Splits a priority queue into two with values going to alternating
    priority queues. The source priority queue is empty when the method
    ends. The order of the values in source is preserved.
    Use: target1, target2 = pq_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
    Returns:
        target1 - a priority queue that contains alternating values
            from source (Priority_Queue)
        target2 - priority queue that contains  alternating values
            from source (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while source.is_empty() != True:
        temp = source.remove()
        target1.insert(temp)
        
        if source.is_empty():
            temp = source.remove()
            target2.insert(temp)
    
    return target1, target2
        

def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    edges = []
    total = 0
    removed = [start_node]
    names = graph.node_names()
    current_edges = []
    
    while len(removed) != len(names):
    
        current_edges = graph.edges_by_node(start_node)
        
        for edge in current_edges:
            
            if edge.end() not in removed:
                pq.insert(edge)
                
        edge = pq.remove()
        
        if edge.end() not in removed:
            edges.append(edge)
            total += edge.distance
            removed.append(edge.end())
            
        start_node = edge.end()
        
    return edges, total


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x - 1, y) + recurse(x, y - 1)
    
    return ans 


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    if m % n == 0:
        ans = n
        
    else:
        ans = gcd(n, m % n)
        
    return  ans


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    
    if len(s) == 0:
        count = 0
    
    else:
        if s[0].lower() in vowels:
            count = 1 + vowel_count(s[1:])
        else:
            count = vowel_count(s[1:])
   
    return count


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    
    if power == 0:
        ans = 1
        
    elif power < 0:
        ans = 1 / base ** (to_power(base, (-1 * power) - 1))
        
    elif power > 0:
        ans = base * to_power(base, power - 1)
        
    return ans


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(s) < 1:
        palindrome = True
    
    else:
        if s[0].isalpha() == False:
            palindrome = is_palindrome(s[1:])
            
        elif s[-1].isalpha() == False:
            palindrome = is_palindrome(s[:-1])
        
        elif s[0].lower() == s[-1].lower():
            palindrome = is_palindrome(s[1:-1])
       
        else:
            palindrome = False
    
    return(palindrome)


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    
    if len(bag) == 0:
        new_set = []
    
    else:
        new_set = bag_to_set(bag[:-1])
        
        if bag[-1] not in new_set:
            new_set.append(bag[-1])
    
    return new_set

