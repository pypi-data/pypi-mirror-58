class numbers:
    def list(start, end, inc=1):

        array = []
        n = start

        if start > end:
            while n >= end:
                array += [n]
                n -= inc
        else:
            while n <= end:
                array += [n]
                n += inc
        
        return array
