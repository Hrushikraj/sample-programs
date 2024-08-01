import xml.etree.ElementTree as ET
#parse XML into element Tree
tree = ET.parse('xml-eg2.xml')
root = tree.getroot()
#root
print(root.tag)
print(len(root))
    #access root child
print(root[0].tag)
print(len(root[0]))
     #loop over root children
for child in root:
    print(child[0].tag)
    print(child[0].text)
    #root Grandchildren
print(root[0][0].tag) #name
print(root[0][0].text) 
print(root[0][1].tag) #age
print(root[0][1].text)
print(root[0][2].tag) #major
print(root[0][2].text) 
print(root[0][3].tag) #courses
print(root[0][3].text)

'''#iterate over each student node
for student in root.findall('student'):
    name = student.find('name').text
    age = student.find('age').text
    major = student.find('major').text
    courses = [course.text for course in student.find('courses').findall('course')]
    #print student details
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Major: {major}")
    print("Courses: " + ", ".join(courses))
    print()  #  newline  '''