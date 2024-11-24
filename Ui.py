from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('TkAgg')  # Use a backend that works well in most environments
import matplotlib.pyplot as plt
import random

# Load the map image
map_image = Image.open("mad-cool/festivalmap.png").convert("RGBA")

# Define grid-based areas with their configurations
grid_areas = {
    "Toilets": {"top_left": (264, 413), "bottom_right": (330, 598), "grid": (10, 5)},  # 10x5 grid
    "Bar 1": {"top_left": (548, 345), "bottom_right": (605, 466), "grid": (3, 3), "remove_center": True},
    "Bar 2": {"top_left": (844, 344), "bottom_right": (904, 466), "grid": (3, 3), "remove_center": True},
    "Foodstand": {"top_left": (764, 144), "bottom_right": (863, 175), "grid": (1, 10)},  # 1x10 grid
    "Merch Stand": {"top_left": (693, 394), "bottom_right": (756, 418), "grid": (1, 5)}  # 1x5 row
}

# Define the stage areas
stage_areas = {
    "stage1": [(422, 606), (587, 606), (587, 718), (422, 718)],
    "stage2": [(792, 616), (957, 616), (957, 729), (792, 729)],
    "stage3": [(568, 141), (670, 141), (670, 200), (568, 200)],
    "stage4": [(1118, 243), (1179, 243), (1179, 369), (1118, 369)]
}

# Function to map a value to a color (green to red)
def value_to_color(value, min_value=0, max_value=100):
    value = max(min_value, min(max_value, value))  # Clamp the value within range
    ratio = (value - min_value) / (max_value - min_value)
    r = int(255 * ratio)
    g = int(255 * (1 - ratio))
    b = 0
    return (r, g, b, 255)  # Full opacity

# Function to divide an area into a grid
def divide_area_into_grid(top_left, bottom_right, rows, cols, remove_center=False):
    x1, y1 = top_left
    x2, y2 = bottom_right
    width = x2 - x1
    height = y2 - y1

    cell_width = width / cols
    cell_height = height / rows

    subareas = []
    for i in range(rows):
        for j in range(cols):
            # Calculate the subarea coordinates
            subarea_top_left = (x1 + j * cell_width, y1 + i * cell_height)
            subarea_bottom_right = (x1 + (j + 1) * cell_width, y1 + (i + 1) * cell_height)

            # Skip the center square if required
            if remove_center and rows == 3 and cols == 3 and i == 1 and j == 1:
                continue

            subareas.append((subarea_top_left, subarea_bottom_right))
    return subareas

# Prepare the subareas for grid-based areas
subareas_data = {}
for name, area in grid_areas.items():
    grid = area["grid"]
    remove_center = area.get("remove_center", False)
    subareas_data[name] = divide_area_into_grid(
        area["top_left"],
        area["bottom_right"],
        grid[0],
        grid[1],
        remove_center
    )

# Main loop to update the image with all functionalities
plt.ion()  # Turn on interactive mode for continuous display

while True:
    # Create a copy of the image to draw on
    map_image_copy = map_image.copy()
    draw = ImageDraw.Draw(map_image_copy, 'RGBA')

    # Simulate values for stage areas
    current_values = {
        "stage1": random.randint(0, 100),
        "stage2": random.randint(0, 100),
        "stage3": random.randint(0, 100),
        "stage4": random.randint(0, 100)
    }

    # Draw the stage areas with colors based on the values
    stage_people_count = 0
    for name, points in stage_areas.items():
        value = current_values[name]
        stage_people_count += value  # Count people in the stages
        color = value_to_color(value)
        draw.polygon(points, fill=color, outline="black", width=3)
        # Calculate the centroid for labeling
        centroid_x = sum(x for x, y in points) // len(points)
        centroid_y = sum(y for x, y in points) // len(points)
        draw.text((centroid_x, centroid_y), f"{value}", fill="black")  # Show value inside the area

    # Draw grid-based areas with random colors
    grid_people_count = 0
    for name, subareas in subareas_data.items():
        for subarea in subareas:
            is_red = random.choice([True, False])
            color = (255, 0, 0, 150) if is_red else (0, 255, 0, 150)
            if is_red:
                grid_people_count += 1  # Count red squares as people
            draw.rectangle(subarea, fill=color, outline="black", width=1)

    # Calculate total people for the progress bar
    total_people = stage_people_count + grid_people_count
    max_capacity = (len(stage_areas) * 100) + sum([len(subareas) for subareas in subareas_data.values()])  # Max capacity

    capacity_percentage = (total_people / max_capacity) * 100

    # Vertical progress bar position and dimensions
    bar_x_start = 70
    bar_y_start = 250
    bar_height = 400
    bar_width = 30
    bar_fill_height = int((capacity_percentage / 100) * bar_height)

    # Draw "Capacity of the Festival" text above the bar
    font = ImageFont.truetype("arial.ttf", 20)  # Use a larger font
    draw.text((bar_x_start, bar_y_start - 40), "Capacity of the Festival", font=font, fill="black")

    # Draw the progress bar background (gray)
    draw.rectangle(
        [bar_x_start, bar_y_start, bar_x_start + bar_width, bar_y_start + bar_height],
        fill="gray"
    )

    # Draw the filled part of the progress bar
    draw.rectangle(
        [bar_x_start, bar_y_start + bar_height - bar_fill_height, bar_x_start + bar_width, bar_y_start + bar_height],
        fill=value_to_color(int(capacity_percentage))
    )

    # Add capacity percentage label
    draw.text((bar_x_start + bar_width + 10, bar_y_start + bar_height - bar_fill_height - 10),
              f"{int(capacity_percentage)}%", fill="black", font=ImageFont.load_default())

    # Simulate random queue lengths
    normal_queue_length = random.randint(0, 100)  # Simulate Normal Queue length
    vip_queue_length = random.randint(0, 100)     # Simulate VIP Queue length
    max_bar_length = 300  # Maximum width of the bars

    # Normal Queue
    normal_bar_top_left = (987, 144)
    normal_bar_bottom_right = (987 + int(normal_queue_length / 100 * max_bar_length), 174)
    draw.text((normal_bar_top_left[0], normal_bar_top_left[1] - 20), "  Normal Queue", fill="black", font=ImageFont.load_default())
    draw.rectangle([normal_bar_top_left, normal_bar_bottom_right], fill=value_to_color(normal_queue_length))

    # VIP Queue
    vip_bar_top_left = (987, 201)
    vip_bar_bottom_right = (987 + int(vip_queue_length / 100 * max_bar_length), 231)
    draw.text((vip_bar_top_left[0], vip_bar_top_left[1] - 20), "  VIP Queue", fill="black", font=ImageFont.load_default())
    draw.rectangle([vip_bar_top_left, vip_bar_bottom_right], fill=value_to_color(vip_queue_length))

    # Display the updated image
    plt.imshow(map_image_copy)
    plt.axis('off')  # Hide axes for better visualization
    plt.draw()  # Draw the updated figure
    plt.pause(0.5)  # Pause to simulate periodic updates
    plt.clf()  # Clear the figure for the next iteration