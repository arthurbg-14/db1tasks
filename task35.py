from this import d
from xml.sax.handler import property_interning_dict


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

finaldict = dic1 | dic2 | dic3

print(finaldict)