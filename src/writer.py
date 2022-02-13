class Writer:
    def writeToFile(self, fileName, data):
        """
        Function to write content into a given file
        params:
            - fileName: name of the file to be written into
            - data: contents that are written into <fileName>
        returns:
            None
        """
        length = data['length']
        files = data['files']
        offsets = data['offsets']
        fp = open(fileName, "w")
        result = "Max length of Strand = " + str(length) + "\n" \
                + "\n".join(["File Name = sample." + str(fName) + " Offset = " + str(off)\
                    for fName, off in zip(files, offsets)])
        print(result)
        fp.write(result)
        fp.close()
        