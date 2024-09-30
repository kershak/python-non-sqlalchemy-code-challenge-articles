#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    
    mag1 = Magazine(name="mag1", category="misc")
    mag2 = Magazine(name="mag2", category="misc")
    mag3 = Magazine(name="mag3", category="misc")
    
    auth1 = Author(name="auth1")
    auth2 = Author(name="auth2")
    auth3 = Author(name="auth3")
    
    art1 = Article(title="hellllo", author=auth1, magazine=mag1)

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
