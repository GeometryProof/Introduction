from manim import *

class GeometryProofsIntro(Scene):
    def construct(self):
        # Set a background color - a dark slate grey for a modern look
        self.camera.background_color = "#2c3e50"
        # 1. Create the shapes
        square = Square(side_length=2.0, color=BLUE)
        triangle = Polygon([-1, -1, 0], [1, -1, 0], [-1, 1, 0], color=GREEN)
        circle = Circle(radius=1.5, color=RED)

        # 2. Animate the drawing of the shapes
        self.play(Create(square), run_time=1.5)
        self.wait(0.5)
        self.play(Create(triangle), run_time=1.5)
        self.wait(0.5)
        self.play(Create(circle), run_time=1.5)
        self.wait(1)

        # 3. Animate the shapes into the logo formation
        self.play(
            triangle.animate.shift(UP * 0.0), # Triangle is already in place
            square.animate.scale(1.0),
            circle.animate.scale(1.2)
        )
        self.wait(0.5)

        # Group the logo elements
        logo = VGroup(square, triangle, circle)

        # 4. Animate the channel name
        channel_name = Text("Geometry Proofs", font_size=48, color=BLACK)
        channel_name.next_to(logo, DOWN, buff=0.5)

        self.play(Write(channel_name))
        self.wait(2)

        # 5. Hold the final scene
        self.play(FadeOut(logo), FadeOut(channel_name))
        self.wait(1)