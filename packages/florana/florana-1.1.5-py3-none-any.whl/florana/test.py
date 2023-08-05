import re
import extract

#pattern = re.compile(r'(0[\)\]]?\s+?m;)', re.DOTALL)
s = """
35b. Cuscuta pacifica Costea & M. A. R. Wright
var. papillata (Yuncker) Costea & M. A. R.
Wright, Syst. Bot. 34: 792. 2009 C E
Cuscuta salina Engelmann var. papillata Yuncker, Bull.
Torrey Bot. Club 69: 543. 1942

Pedicels papillate. Calyces papillate.
Flowering Jul--Oct. Hosts: Lupinus littoralis var.
variicolor and other herbs; coastal interdune
depressions and grasslands; of conservation concern; 0-10 m; Calif.

"""
print(extract.loc_text_pattern.findall(s))
for loc in extract.locs_in(s):
    print(loc)
