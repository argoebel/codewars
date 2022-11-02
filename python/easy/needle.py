def find_needle(haystack):
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            return "found the needle at position %i" % i

def find_needle_best(haystack): return 'found the needle at position %d' % haystack.index('needle')
    

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))