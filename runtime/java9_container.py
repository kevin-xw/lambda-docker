
import basic_container

class Java9Container(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "java:9"
	self.command = 'sh -c "javac main.java && java main"'
	self.file_extension = ".java"

