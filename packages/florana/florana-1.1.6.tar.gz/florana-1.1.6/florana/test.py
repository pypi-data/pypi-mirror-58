import extract
import re

fn = 'Cuscuta05g.CH_map.pdf'
text = extract.load_treatment(fn)
genus = extract.genus_in(text)

loc_text_pattern = re.compile(r'0[\)\]]?\s+?m;.*?(?<!Nfld|Labr)'+
                              r'\.\s*?(?:\n|$)', re.DOTALL|re.MULTILINE)
for block, name in extract.partition(text, genus):
    if 'jepsonii' in name:
        #print(', '.join(extract.loc_text_pattern.findall(block)))
        print(', '.join(extract.locs_in(block)))
