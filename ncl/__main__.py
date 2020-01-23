from ncl import *

"""import sys
print("Console args[1] = " + sys.argv[1])"""
print("Create a simple Example:")
print("""from ncl import *
nclCode = Ncl(\"nclv1\", \"http://www.ncl.org.br/NCL3.0/EDTVProfile\")

region = Region(id=\"regImage\", height=\"15%\", width=\"100%\", top=\"0\", left=\"10%\", zIndex=\"10\")
descriptor = Descriptor(id=\"descImage\", region=\"regImage\")
media = Media(id=\"image\", descriptor=\"descImage\", src=\"lena.jpg\")
port = Port(id=\"pImage\", component=\"image\")

region2 = Region(id=\"regImage2\", height=\"15%\", width=\"100%\", top=\"0\", left=\"10%\", zIndex=\"10\")
descriptor2 = Descriptor(id=\"descImage2\", region=\"regImage2\")
media2 = Media(id=\"image2\", descriptor=\"descImage2\", src=\"lena.jpg\")
port2 = Port(id=\"pImage2\", component=\"image2\")

nclCode.add(region)
nclCode.add(descriptor)
nclCode.add(media)
nclCode.add(port)

nclCode.add(region2)
nclCode.add(descriptor2)
nclCode.add(media2)
nclCode.add(port2)
print(nclCode.generate())
          
generate this File file:
          
""")
nclCode = Ncl("nclv1", "http://www.ncl.org.br/NCL3.0/EDTVProfile")

region = Region(id="regImage", height="15%", width="100%", top="0", left="10%", zIndex="10")
descriptor = Descriptor(id="descImage", region="regImage")
media = Media(id="image", descriptor="descImage", src="lena.jpg")
port = Port(id="pImage", component="image")

region2 = Region(id="regImage2", height="15%", width="100%", top="0", left="10%", zIndex="10")
descriptor2 = Descriptor(id="descImage2", region="regImage2")
media2 = Media(id="image2", descriptor="descImage2", src="lena.jpg")
port2 = Port(id="pImage2", component="image2")

nclCode.add(region)
nclCode.add(descriptor)
nclCode.add(media)
nclCode.add(port)

nclCode.add(region2)
nclCode.add(descriptor2)
nclCode.add(media2)
nclCode.add(port2)
print(nclCode.generate())
