import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import random

# Define the grid dimensions
width, height = 100, 80
subgrid_width, subgrid_height = 10, 8  # Subgrid size

# Create a blank canvas for the grid
grid = np.zeros((height, width))

# Define values for each element
TREE = 1
PATH = 2
RIVER = 3
BRIDGE = 4
RUINS = 5
RUNE = 6

# Function to create a main path from the border to the center
def create_main_path(x, y, length, direction):
    if length <= 0 or not (0 <= x < width and 0 <= y < height):
        return
    
    # Mark the current position as part of the path
    grid[y, x] = PATH
    
    # Randomly branch off
    if random.random() < 0.3:  # 30% chance to branch
        branch_x = x + random.choice([-1, 0, 1])
        branch_y = y + random.choice([-1, 0, 1])
        create_main_path(branch_x, branch_y, random.randint(3, 6), direction)
    
    # Continue moving in the same direction
    if direction == "horizontal":
        create_main_path(x + random.choice([-1, 0, 1]), y, length - 1, direction)
    else:
        create_main_path(x, y + random.choice([-1, 0, 1]), length - 1, direction)

# Create the main path from a random border point
border_side = random.choice(["top", "bottom", "left", "right"])
if border_side == "top":
    start_x = random.randint(0, width - 1)
    start_y = 0
    direction = "vertical"
elif border_side == "bottom":
    start_x = random.randint(0, width - 1)
    start_y = height - 1
    direction = "vertical"
elif border_side == "left":
    start_x = 0
    start_y = random.randint(0, height - 1)
    direction = "horizontal"
else:  # right
    start_x = width - 1
    start_y = random.randint(0, height - 1)
    direction = "horizontal"

# Set the path length for the main path
main_path_length = random.randint(15, 30)

# Create the main path
create_main_path(start_x, start_y, main_path_length, direction)

# Populate the grid with trees (70% trees) in empty spaces
for y in range(height):
    for x in range(width):
        if grid[y, x] == 0 and random.random() < 0.7:  # Only fill empty spaces
            grid[y, x] = TREE

# Create rivers (horizontal and vertical lines)
for _ in range(random.randint(3, 6)):  # 3 to 6 rivers
    if random.choice([True, False]):  # Horizontal river
        y = random.randint(0, height - 1)
        for x in range(width):
            grid[y, x] = RIVER
    else:  # Vertical river
        x = random.randint(0, width - 1)
        for y in range(height):
            grid[y, x] = RIVER

# Add bridges across rivers
for _ in range(20):  # 20 bridges
    x, y = random.randint(0, width - 1), random.randint(0, height - 1)
    if grid[y, x] == RIVER:
        grid[y, x] = BRIDGE

# Place some ruins
for _ in range(10):  # 10 ruins
    x, y = random.randint(0, width - 1), random.randint(0, height - 1)
    grid[y, x] = RUINS

# Place some runes
for _ in range(15):  # 15 runes
    x, y = random.randint(0, width - 1), random.randint(0, height - 1)
    grid[y, x] = RUNE

# Define color map for visualization
cmap = mcolors.ListedColormap([
    'white',      # Empty space (0)
    'green',      # Tree (1)
    'tan',        # Path (2)
    'blue',       # River (3)
    'brown',      # Bridge (4)
    'grey',       # Ruins (5)
    'purple'      # Runes (6)
])

# Function to count items in each subgrid
def count_items_in_subgrids(grid, subgrid_width, subgrid_height):
    item_counts = {
        'Trees': [],
        'Paths': [],
        'Rivers': [],
        'Bridges': [],
        'Ruins': [],
        'Runes': []
    }

    # Calculate number of subgrids along width and height
    num_subgrids_x = width // subgrid_width
    num_subgrids_y = height // subgrid_height

    for j in range(num_subgrids_y):
        for i in range(num_subgrids_x):
            subgrid = grid[j * subgrid_height:(j + 1) * subgrid_height, i * subgrid_width:(i + 1) * subgrid_width]
            trees_count = np.sum(subgrid == TREE)
            paths_count = np.sum(subgrid == PATH)
            rivers_count = np.sum(subgrid == RIVER)
            bridges_count = np.sum(subgrid == BRIDGE)
            ruins_count = np.sum(subgrid == RUINS)
            runes_count = np.sum(subgrid == RUNE)
            
            item_counts['Trees'].append(trees_count)
            item_counts['Paths'].append(paths_count)
            item_counts['Rivers'].append(rivers_count)
            item_counts['Bridges'].append(bridges_count)
            item_counts['Ruins'].append(ruins_count)
            item_counts['Runes'].append(runes_count)

    return item_counts

# Count items in the 10x8 grids
item_counts = count_items_in_subgrids(grid, subgrid_width, subgrid_height)

# Print the item counts for each subgrid
for item, counts in item_counts.items():
    print(f"{item}: {counts}")

# Plot the grid with subgrid divisions
plt.figure(figsize=(10, 8))
plt.imshow(grid, cmap=cmap, origin='upper')
plt.grid(which='both', color='black', linestyle='-', linewidth=0.5)  # Add gridlines
plt.xticks(np.arange(-0.5, width, 1), [])  # Hide x-axis labels
plt.yticks(np.arange(-0.5, height, 1), [])  # Hide y-axis labels

# Save the figure as an image
plt.savefig('forest_grid_with_subgrids.png', bbox_inches='tight')  # Save the figure
plt.show()  # Show the plot
