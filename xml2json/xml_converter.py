from xml.dom import minidom
xmldoc = minidom.parse('client_side_attack.xml')


directive_name = xmldoc.getElementsByTagName('directive')
sid_list = xmldoc.getElementsByTagName('rule')
name = xmldoc.getElementsByTagName('name')

print(directive_name[0].attributes['name'].value)
#print(len(sid_list))
print(sid_list[0].attributes['plugin_sid'].value)
#for s in itemlist:
 #   print(s.attributes['plugin_sid'].value)


## Example 

#<data>
#    <items>
#        <item name="item1"></item>
#        <item name="item2"></item>
#        <item name="item3"></item>
#        <item name="item4"></item>
#    </items>
#</data>


#for %s in directive_name[0].attributes['name'].value:
filePath = 'suri-sigma/%s.txt' % (directive_name[0].attributes['name'].value)

with open(filePath, 'w') as text_file:
        text_file.write("title: ")
        text_file.write(directive_name[0].attributes['name'].value)
        text_file.write("description: ")
        text_file.write(directive_name[0].attributes['name'].value)
