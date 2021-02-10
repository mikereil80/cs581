# Author:  Michael Reilly

# Purpose of Program: To process .csv files and form triads based on the opinions of epinion users.

# The program accepts a prompted filename from the user as input, as can be seen by how to run from the terminal window.
# Then it finds all self-loops in the triads, counts them, but do not add to traid analysis.
# Since this will use networkx, that should not be a problem.
# Count the number of positive and negative reviews to create an expected distributions of four triad types for comparison to the actual distribution.
# For expected distribution assume positive and negative trust values are randomly assigned.
# Identify the triads in the graph, for each triad, and must know value of edges in the triangle formed by the three nodes. 
# Identify which of the four triad types it represents and add to appropriate count.
# Output will contain: 
# 1. Number of edges in the network
# 2. Number of self-loops
# 3. Number of edges used to identify triads (TotEdges)[edges - self-loops]
# 4. Number of positive edges (ignore self-loops)
# 5. Number of negative edges (ignore self-loops)
# 6. Probability p that an edge will be positive: (number of positive edges)/TotEdges
# 7. Probability that an edge will be negative: 1-p
# 8. Expected distribution of triad types (based on p and 1-p applied to the number of triangles in the graph). Show number and percent.
    # a. Trust-Trust-Trust b. Trust-Trust-Distrust c. Trust-Distrust-Distrust d. Distrust-Distrust-Distrust e. Total
# 9. Actual distribution of triad types. Show number and percent.
    # a. Trust-Trust-Trust b. Trust-Trust-Distrust c. Trust-Distrust-Distrust d. Distrust-Distrust-Distrust e. Total
# 

# The implementation I did using networkx was unable to do the epinions.csv file, so the only outputs are epinion96.csv and epionion_small.csv files

# To run from terminal window:   python3 Reilly_HW5.py filename

import networkx as nx
from itertools import combinations as comb
import argparse


#  function triad_processing retrieves the data of the .csv file and processes all the possible triads.

def triad_processing(f_name):
    # universal variables for the number of positive edges, negative edges, self_loops, and total edges
    num_of_positives=0
    num_of_negatives=0
    num_of_self_loops=0
    num_of_edges=0
    # make an empty graph where all the triads will be placed
    Graph=nx.Graph()
    # reads the csv file row by row and collects the data
    with open(f_name, "r") as triads_file:
        for row in triads_file:
            # Makes a list of three values, the reviewer, the reviewee, and the weight of the relationship
            reviewer, reviewee, weight=list(map(int, row.split(",")))
            # Put in the graph the nodes as well as the edge between them for future reference
            Graph.add_node(reviewer)
            Graph.add_node(reviewee)
            Graph.add_edge(reviewer, reviewee, weight=weight)
            # self_loop counter
            if(reviewer==reviewee):
                num_of_self_loops+=1
    
    # Based on weighted graph documentation at: https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
    for (reviewer, reviewee, weight) in Graph.edges(data=True):
        if(weight["weight"]==1):
            num_of_positives+=1
        if(weight["weight"]==-1):
            num_of_negatives+=1

    # built-in function in networkx to count the number of edges
    num_of_edges=Graph.number_of_edges()
    print("\nEdges in network: "+str(num_of_edges))

    print("Self-loops: "+str(num_of_self_loops))

    # TotEdges=(all edges-self loops)
    TotEdges=(num_of_edges-num_of_self_loops)
    print("Edges used - TotEdges: "+str(TotEdges))

    # Check all edges for their weight
    print("trust edges: "+str(num_of_positives))

    # P(Trust)=Positives/TotEdges
    p_positive=(num_of_positives/num_of_edges)
    print("probability p: {:.2f}".format(p_positive))

    print("distrust edges: "+str(num_of_negatives))

    # P(Distrust)=Negatives/TotEdges
    p_negative=(num_of_negatives/num_of_edges)
    print("probability 1-p: {:.2f}".format(p_negative))

    # Networkx has a builtin triangles function which creates a dictionary of all the triangles
    # Each triangle is counted 3 times (for each node) so total dictionary entries/3 is the number of triangles
    # This information found: https://stackoverflow.com/questions/60426256/finding-total-number-of-triangles-using-networkx
    trianglex3=nx.triangles(Graph)
    num_of_triangles=sum(trianglex3.values())/3
    print("Triangles: {:.0f}".format(num_of_triangles))

    print("\nExpected Distribution")
    print("Type\tpercent\tnumber")

    # Expected Values for TTT, only one combo so no *3
    # percent=All p's multiplied together
    # number=percent*all triangles
    TTT_percent=(p_positive*p_positive*p_positive)
    TTT_number=(num_of_triangles*TTT_percent)
    print("TTT\t{:.1f}".format(TTT_percent*100)+"\t{:.1f}".format(TTT_number))
    
    # Expected Values for TTD, 3 combos TTD TDT DTT
    TTD_percent=((p_positive*p_positive*p_negative)*3)
    TTD_number=(num_of_triangles*TTD_percent)
    print("TTD\t{:.1f}".format(TTD_percent*100)+"\t{:.1f}".format(TTD_number))

    # Expected Values for TDD, 3 comboes TDD DTD DDT
    TDD_percent=((p_positive*p_negative*p_negative)*3)
    TDD_number=(num_of_triangles*TDD_percent)
    print("TDD\t{:.1f}".format(TDD_percent*100)+"\t{:.1f}".format(TDD_number))

    # Expected Values for DDD, only one combo
    DDD_percent=(p_negative*p_negative*p_negative)
    DDD_number=(num_of_triangles*DDD_percent)
    print("DDD\t{:.1f}".format(DDD_percent*100)+"\t{:.1f}".format(DDD_number))

    # Expected totals
    Total_percent=(TTT_percent+TTD_percent+TDD_percent+DDD_percent)
    Total_number=(round(TTT_number,1)+round(TTD_number,1)+round(TDD_number,1)+round(DDD_number,1))
    print("Total\t{:.0f}".format(Total_percent*100)+"\t{:.1f}".format(Total_number))

    # variables for each type of Triad possible
    num_of_TTT=0
    num_of_TTD=0
    num_of_TDD=0
    num_of_DDD=0
    # get_edge_attributes is a networkx function that finds the name of an attribute in the graph
    weight=nx.get_edge_attributes(Graph, 'weight')
    # finds all graphs of size 3, all triads
    all_triads=[i for i in nx.enumerate_all_cliques(Graph) if(len(i)==3)]
    # listifies it based on: https://networkx.org/documentation/networkx-1.10/reference/generated/networkx.algorithms.clique.enumerate_all_cliques.html, since need to get all sets of 3
    list_of_triads=list(map(lambda i: list(map(lambda i: (i, weight[i]), comb(i,2))), all_triads))

    # the indices of the list, get all 3 weights
    for index in list_of_triads:
        weight1=index[0][1]
        weight2=index[1][1]
        weight3=index[2][1]

        # all 3 weights are 1, TTT
        if(weight1==1 and weight2==1 and weight3==1):
            num_of_TTT+=1
        # 2 weights are 1, 1 weight is -1, TTD, all 3 possibile combos
        if(weight1==1 and weight2==1 and weight3==-1):
            num_of_TTD+=1
        if(weight1==1 and weight2==-1 and weight3==1):
            num_of_TTD+=1
        if(weight1==-1 and weight2==1 and weight3==1):
            num_of_TTD+=1
        # 1 weight is -1, 2 weights are 1, TDD, all 3 possibile conbos
        if(weight1==1 and weight2==-1 and weight3==-1):
            num_of_TDD+=1
        if(weight1==-1 and weight2==1 and weight3==-1):
            num_of_TDD+=1
        if(weight1==-1 and weight2==-1 and weight3==1):
            num_of_TDD+=1
        # all 3 weights are -1, DDD
        if(weight1==-1 and weight2==-1 and weight3==-1):
            num_of_DDD+=1

    print("\nActual Distribution")
    print("Type\tpercent\tnumber")

    # % is count of TTT divided by all triangles
    percent_of_TTT=(num_of_TTT/num_of_triangles)
    print("TTT\t{:.1f}".format(percent_of_TTT*100)+"\t"+str(num_of_TTT))

    # % is count of TTD divided by all triangles
    percent_of_TTD=(num_of_TTD/num_of_triangles)
    print("TTD\t{:.1f}".format(percent_of_TTD*100)+"\t"+str(num_of_TTD))

    # % is count of TDD divided by all triangles
    percent_of_TDD=(num_of_TDD/num_of_triangles)
    print("TDD\t{:.1f}".format(percent_of_TDD*100)+"\t"+str(num_of_TDD))

    # % is count of DDD divided by all triangles
    percent_of_DDD=(num_of_DDD/num_of_triangles)
    print("DDD\t{:.1f}".format(percent_of_DDD*100)+"\t"+str(num_of_DDD))

    # Totals are just an add of TTT, TTD, TDD, and DDD components
    percent_of_Total=(percent_of_TTT+percent_of_TTD+percent_of_TDD+percent_of_DDD)
    num_of_Total=(num_of_TTT+num_of_TTD+num_of_TDD+num_of_DDD)
    print("Total\t{:.0f}".format(percent_of_Total*100)+"\t"+str(num_of_Total))


# main routine
if __name__ == "__main__":   
    # argparse will parse the arguments passed in through command line
    parser=argparse.ArgumentParser(description="Triad Data Collection from epinions.")
    # The argument we are looking for, filename
    parser.add_argument("filename", default="fake.csv")
    # parse_args on parser to get a usable version of the results
    fileName=parser.parse_args()
    # the function to start using the data
    triad_processing(fileName.filename)
