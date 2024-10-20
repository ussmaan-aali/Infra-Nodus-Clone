import nltk
import networkx as nx
from collections import defaultdict
from pyvis.network import Network 


def draw_graph(text):

    # Tokenize the text into words
    tokens = nltk.word_tokenize(text)
    
    bigrams = [(tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1)]
    four_grams = [(tokens[i], tokens[i + 1], tokens[i + 2], tokens[i + 3]) for i in range(len(tokens) - 3)]

    # Construct edges with respective weights for bigrams
    edges = {edge: 3 for edge in bigrams}

    # Adding second layer of connections with weights for 4-grams
    for gram in four_grams:
        # one word apart
        edges[(gram[0], gram[2])] = 2
        edges[(gram[1], gram[3])] = 2 

        # two word apart
        edges[(gram[0], gram[3])] = 1


    # Create a directed graph
    G = nx.DiGraph()

    # Add edges to the graph with their respective weights
    for edge, weight in edges.items():
        G.add_edge(edge[0], edge[1], weight=weight)

    scale=2 # Scaling the size of the nodes by 10*degree
    d = dict(G.degree)

    #Updating dict
    d.update((x, scale*y) for x, y in d.items())

    #Setting up size attribute
    nx.set_node_attributes(G,d,'size')

#     pos = nx.spring_layout(G)

#     from networkx.algorithms.community.modularity_max import greedy_modularity_communities
    
#     topics = list(greedy_modularity_communities(G))

    colors = [
    '#FF0000',  # Red
    '#00FF00',  # Green
    '#0000FF',  # Blue
    '#FFFF00',  # Yellow
    '#FF00FF',  # Magenta
    '#00FFFF',  # Cyan
    '#800080',  # Purple
    '#FFA500',  # Orange
    '#008000',  # Dark Green
    '#800000'   # Maroon
        ]


    net = Network(height='625px', 
        width = "100%", 
        bgcolor='#222222', 
        font_color='white',
        cdn_resources='remote',
    )

    net.from_nx(G)

#     node_color = {}  # Dictionary to store node colors
#     for idx, topic in enumerate(topics):
#         for node in topic:
#             node_color[node] = colors[idx]

#     net.set_node_attributes(node_color, name='color')
    
#     net.show_buttons(filter_=["edges"])

    net.set_options("""{
    "nodes": {
            "borderWidth": 0,
            "color": {
            "border": "#2B7CE9",
            "background": "#97C2FC",
            "highlight": {
                    "border": "#66fa89",
                    "background": "#66fa89"
            }
            },
            "font": {
            "size": 45,
            "face": "verdana"
            },
            "scaling": {
            "min": 89
            },
            "size": null
    },
    "edges": {
            "color": {
            "inherit": false
            },
            "selfReferenceSize": null,
            "selfReference": {
            "angle": 0.7853981633974483
            },
            "smooth": {
            "forceDirection": "none"
            }
    },
    "interaction": {
            "hover": true,
            "hoverConnectedEdges": true,
            "multiselect": true,
            "navigationButtons": true
    },
    "physics": {
            "forceAtlas2Based": {
            "centralGravity": 0.05,
            "springLength": 100
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based"
    }
    }
    """)
#     net.set_options("""{
#         "interaction": {
#                 "hover": true,
#                 "hoverConnectedEdges": true,
#                 "multiselect": true,
#                 "navigationButtons": true
#         },
#         "physics": {
#                 "forceAtlas2Based": {
#                 "centralGravity": 0.05,
#                 "springLength": 100
#                 },
#                 "minVelocity": 0.75,
#                 "solver": "forceAtlas2Based"
#         }
#         }
#         """)


    # net.show_buttons()

    path = 'D:/Muaz_AI_Consultant/textNetworkGraph/html_files'
    net.save_graph(f'{path}/pyvis_graph.html')

    return True