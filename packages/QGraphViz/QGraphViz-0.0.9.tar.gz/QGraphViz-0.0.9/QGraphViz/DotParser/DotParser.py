#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Saifeddine ALOUI
Description:
Dot perser implementation
"""
from QGraphViz.DotParser.Graph import Graph, GraphType
from QGraphViz.DotParser.Node import Node
from QGraphViz.DotParser.Edge import Edge

class DotParser():
    """
    The dot language parser
    """
    def __init__(self):
        pass
    def split(self, s):
        parts = []
        bracket_level = 0
        current = []
        # trick to remove special-case of trailing chars
        for c in (s + ","):
            if c == "," and bracket_level == 0:
                parts.append("".join(current))
                current = []
            else:
                if c == "{":
                    bracket_level += 1
                elif c == "}":
                    bracket_level -= 1
                current.append(c)
        return parts    
    def find_params(self, data):
        try:
            start_idx=data.index("[")
            end_index=data.rindex("]")

            strparams = self.split(data[start_idx+1:end_index])#.split(",")

            params={}
            for param in strparams:
                vals = param.split("=")
                params[vals[0].strip()] = vals[1].strip()
            return params, start_idx, end_index
        except:
            return None, 0, 0
    def parse_subdata(self, data, graph):
        try:
            end_index=data.index(";")
            sub_data = data[:end_index]
            try:
                link_idx=sub_data.index("--")
                # find parameters

                source_node_name = sub_data[:link_idx].strip()
                dest_node_name = sub_data[link_idx+3:end_index].strip()
                source_node  = graph.getNodeByName(source_node_name)
                dest_node  = graph.getNodeByName(dest_node_name)
                if(source_node is not None and dest_node is not None):
                    edge = Edge(source_node, dest_node)
                    graph.edges.append(edge)
            except:
                try:
                    params, params_start_idx, params_end_index =self.find_params(sub_data)
                    if(params is not None):
                        subname = data[0:params_start_idx].strip()
                    else:
                        subname = data[0:end_index].strip()

                    node = Node(subname)
                    node.kwargs = params
                    graph.nodes.append(node)


                except:
                    pass
            if(end_index<len(data)):
                self.parse_subdata(data[end_index+1:], graph)
        except:
            pass

    def parseFile(self, filename):
        graph=Graph()
        with open(filename,"r") as fi:
            data=fi.read()
            try:
                graph_idx= data.index("dgraph")
                print("found dgraph at {}".format(graph_idx))
                graph=Graph(GraphType.DirectedGraph)
            except:
                try:
                    graph_idx= data.index("graph")
                    print("found dgraph at {}".format(graph_idx))
                    graph=Graph()
                except:
                    raise Exception("Syntax error")
            data=data[graph_idx+5:]
            start_id=data.index("{")
            end_id=data.rindex("}")
            self.parse_subdata(data[start_id+1:end_id], graph)
        return graph


    def save(self, filename, graph):
        with open(filename,"w") as fi:
            if graph.graph_type == GraphType.SimpleGraph:
                fi.write("graph {\n")
                for node in graph.nodes:
                    fi.write("    {} [{}];\n".format(node.name, ",".join(["{}={}".format(k,v) for k,v in node.kwargs.items()])))
                for edge in graph.edges:
                    fi.write("    {} -- {};\n".format(edge.source.name, edge.dest.name))
                fi.write("}")
            if graph.graph_type == GraphType.DirectedGraph:
                fi.write("dgraph {\n")
                for node in graph.nodes:
                    fi.write("    {} [{}];\n".format(node.name, ",".join(["{}={}".format(k,v) for k,v in node.kwargs.items()])))
                for edge in graph.edges:
                    fi.write("    {} -> {};\n".format(edge.source.name, edge.dest.name))
                fi.write("}")
