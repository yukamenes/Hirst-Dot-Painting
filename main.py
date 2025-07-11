import colorgram
import turtle
import random
import os

"""Generate a Damien Hirst-inspired dot painting using colors extracted from an image."""

turtle.colormode(255)  # Set color mode to RGB (0-255)

# Initialize turtle
t1 = turtle.Turtle()
t1.speed(0)  # Set fastest drawing speed
t1.up()  # Lift pen to avoid drawing lines
t1.goto(-285, -270)  # Move to starting position
t1.down()  # Lower pen for drawing dots

# Extract colors from image.jpg and filter out near-white colors
try:
    if not os.path.exists('image.jpg'):
        raise FileNotFoundError("Image file 'image.jpg' not found. Please provide a valid image file.")
    
    colors = colorgram.extract('image.jpg', 30)  # Extract 30 colors from image
    rgb_colors = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors if not (c.rgb.r > 230 and c.rgb.g > 230 and c.rgb.b > 230)]
    
    if not rgb_colors:
        raise ValueError("No valid colors extracted from the image. Try a different image or adjust the RGB threshold.")

    # Draw a 15x12 grid of colored dots
    for _ in range(15):  # 15 rows
        for _ in range(12):  # 12 columns
            t1.dot(20, random.choice(rgb_colors))  # Draw a 20-pixel dot with random color
            t1.up()  # Lift pen to move without drawing
            t1.fd(50)  # Move forward 50 pixels
        # Alternate direction for zigzag pattern
        if t1.heading() == 0:
            t1.setheading(180)
        elif t1.heading() == 180:
            t1.setheading(0)
        t1.fd(50)  # Move to start of next row
        t1.goto(t1.xcor(), t1.ycor() + 40)  # Move up 40 pixels for next row
    t1.hideturtle()  # Hide turtle cursor

    # Display window and exit on click
    screen = turtle.Screen()
    screen.exitonclick()

except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")