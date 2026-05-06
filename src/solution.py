import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 1. READ THE DATASET AND CREATE THE GRAPH
df = pd.read_csv("data/network_data.csv")
G = nx.Graph()

for index, row in df.iterrows():
    G.add_edge(row['Source'], row['Target'], weight=row['Weight'])

# 2. DEFINE THE SOURCE NODE (HEADQUARTERS)
source_node = "Fatih"

# Calculate shortest paths and times to all nodes from the source
lengths, paths = nx.single_source_dijkstra(G, source=source_node, weight='weight')

# Print a managerial report to the terminal
print("\n" + "="*65)
print(f" IT FIELD SERVICE - EMERGENCY ROUTING REPORT (HUB: {source_node.upper()})")
print("="*65)

for target, time in sorted(lengths.items(), key=lambda x: x[1]):
    if target != source_node:
        route_str = " -> ".join(paths[target])
        print(f"Target: {target.ljust(10)} | Time: {str(time).rjust(2)} mins | Route: {route_str}")
print("="*65 + "\n")


# Determine the layout once so all maps look consistent
# 3. VISUALIZATION AND SAVING MULTIPLE IMAGES

# Define exact geographic positions for each district (x, y) to prevent crossing branches
# European side is on the left (-x), Asian side is on the right (+x)
custom_pos = {
    "Kagithane": (-2, 3),
    "Besiktas": (-1, 2),
    "Fatih": (-2, -1),
    "Uskudar": (1, 1),
    "Kadikoy": (1, -1),
    "Umraniye": (3, 2),
    "Atasehir": (3, 0)
}

pos = custom_pos # Use our custom realistic map layout instead of spring_layout

print("Generating and saving individual route maps...")

print("Generating and saving individual route maps...")

for target, path in paths.items():
    # Skip creating a map for Fatih to Fatih
    if target == source_node:
        continue
        
    time = lengths[target]
    
    plt.figure(figsize=(10, 7))
    
    # Draw the base network in light gray
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=3000, 
            font_size=10, font_weight='bold', edge_color='gainsboro')
    
    # Identify the edges used in the specific shortest path
    path_edges = list(zip(path, path[1:]))
    
    # Highlight the specific route (Green nodes, Red edges)
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='lightgreen', node_size=3000)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3.5)
    
    # Add weight (minute) labels to the edges
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
    
    # Set the English title for the specific route
    plt.title(f"Shortest Path from {source_node} to {target} ({time} mins)", fontsize=14, fontweight='bold')
    
    # Create a dynamic file name and save it to the results folder
    file_name = f"results/route_{source_node}_to_{target}.png"
    plt.savefig(file_name)
    
    # IMPORTANT: Close the plot so the next route doesn't draw on top of this one
    plt.close()

print("All maps have been successfully saved in the 'results/' folder!")