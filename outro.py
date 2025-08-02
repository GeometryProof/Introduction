from manim import *

class GeometryProofsBanner(Scene):
    def construct(self):
        # Set a background color - a dark slate grey for a modern look
        self.camera.background_color = "#2c3e50"

        # --- Safe Area Visualization (optional, for testing) ---
        # YouTube banner safe area is roughly 1546x423 pixels in a 2560x1440 image.
        # Manim's default scene is 8 units high and 14.22 units wide.
        # We can approximate the safe area for positioning.
        safe_area = Rectangle(
            width=14.22 * (1546 / 2560),
            height=8 * (423 / 1440),
            stroke_color=RED,
            stroke_width=2
        )
        # self.add(safe_area) # Uncomment to see the safe area

        # --- Animated Background Elements ---
        lines = VGroup()
        for i in range(15):
            line = Line(
                start=np.array([-9, np.random.uniform(-5, 5), 0]),
                end=np.array([9, np.random.uniform(-5, 5), 0]),
                stroke_color=BLUE,
                stroke_opacity=0.3,
                stroke_width=1
            )
            lines.add(line)

        self.play(Create(lines), run_time=2)

        # --- Channel Name and Tagline ---
        channel_name = Text("Geometry Proofs", font_size=96, color=WHITE)
        tagline = Text("Elegant. Rigorous. Visual.", font_size=48, color=LIGHT_GREY)
        
        # Position the text within the safe area
        channel_name.move_to(ORIGIN)
        tagline.next_to(channel_name, DOWN, buff=0.5)

        self.play(Write(channel_name), run_time=2)
        self.play(FadeIn(tagline, shift=UP), run_time=1.5)

        # --- Looping Animation ---
        self.play(
            lines.animate.shift(UP * 2).set_opacity(0.1),
            rate_func=linear,
            run_time=5
        )
        self.play(
            lines.animate.shift(DOWN * 2).set_opacity(0.3),
            rate_func=linear,
            run_time=5
        )

        # Keep the final banner elements on screen
        self.wait(3)