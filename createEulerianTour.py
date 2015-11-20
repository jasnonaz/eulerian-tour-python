    # Find Eulerian Tour
    #
    # Write a function that takes in a graph
    # represented as a list of tuples
    # and return a list of nodes that
    # you would follow on an Eulerian Tour
    #
    # For example, if the input graph was
    # [(1, 2), (2, 3), (3, 1)]
    # A possible Eulerian tour would be [1, 2, 3, 1]
    import random

    def find_eulerian_tour(graph):
        # your code here
        tour = []
        degreeDict = calcFrequency(graph)
        connectome = createConnectome(graph)
        startFinishValues = startFinish(degreeDict)
        start = startFinishValues[0]
        end = startFinishValues[1]
        nodes = connectome.keys()
        spot = connectome[start][0]
        tour.append(start)
        tour.append(connectome[start][0])
        connectome = removeConnections(connectome,start,connectome[start][0])
        while(len(connectome[end]) > 0):
            print('starting loop')
            oldSpot = spot
            if len(connectome[spot]) > 1:
                print('test1')
                print(len(connectome[spot]))
                for node in connectome[spot]:
                    if node != end and node != spot:
                        spot = node
            else:
                spot = connectome[spot][0]
            print("spot is " + str(spot))
            print(connectome)
            tour.append(spot)
            connectome = removeConnections(connectome,spot,oldSpot)
        return tour

    def calcFrequency(graph):
        degreeDict = {}
        for edge in graph:
            for node in edge:
                if node not in degreeDict:
                    degreeDict[node] = 1
                else:
                    degreeDict[node] = degreeDict[node] + 1
        return degreeDict

    def createConnectome(graph):
        connectome = {}
        for edge in graph:
            if edge[0] in connectome:
                connectome[edge[0]].append(edge[1])
            if edge[1] in connectome:
                connectome[edge[1]].append(edge[0])        
            if edge[0] not in connectome:
                connectome[edge[0]] = [edge[1]]
            if edge[1] not in connectome:
                connectome[edge[1]] = [edge[0]]
        return(connectome)

    def startFinish(degreeDict):
        numOdds = 0
        for node in degreeDict:
            degree = degreeDict[node]
            if degree % 2 == 1:
                if numOdds == 0:
                    start = node
                if numOdds == 1:
                    end = node
                numOdds = numOdds+1
        if numOdds == 0:
            counter = 0
            for node in degreeDict:
                if counter == 0:
                    start = node
                    end = node
                counter = counter + 1
            return [start,end]
        if numOdds == 1:
            return "No possible solution"
        else:
            return [start,end]

    def removeConnections(connectome,first,second):
        connectome[first].remove(second)
        connectome[second].remove(first)
        return connectome
