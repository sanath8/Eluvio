class Reader:
    def readFile(self, i):
        """
        Function to read the contents of a given file
        Params:
            - i: index of the file represented as sample.i
        Returns:
            - the contents of the file <sample.i>
        """
        f = open('../Eluvio Challenge - Core Engineering/sample.' + str(i))
        contents = f.readlines()
        f.close()
        return "".join(contents)
        
    