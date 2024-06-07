#!/bin/false
#META/description=Replacements for Perl's chop and chomp.
#META/language=Python



def chop(s):
    "Returns a tuple of (chopped string, removed char)"
    return (s[:-1],s[len(s)-1])

def chomp(s,charsToRemove=[]):
    charsRemoved = []
    canRemoveChar = True
    
    # check each char to see if it is at the end of s
    while canRemoveChar:
        charRemoved = False
        
        for c in charsToRemove:
            if (c == s[len(s)-1]):
                # can remove char
                charRemoved = True

                # remove char
                s = s[:-1]

                charsRemoved.append(c)
        # if cannot remove any character at end, we are finished.

        if (charRemoved == False):
            canRemoveChar = False

    return (s,charsRemoved)
    
