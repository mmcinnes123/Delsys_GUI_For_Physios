from vispy import gloo
from vispy import app
import numpy as np


class SimplePlot(app.Canvas):
    def __init__(self, plot_mode: str = 'windowed'):
        app.use_app('PySide6')
        app.Canvas.__init__(self, title='Simple Plot',
                            keys='interactive', app='PySide6')
        gloo.set_viewport(0, 0, *self.physical_size)
        gloo.set_state(clear_color='black', blend=True,
                       blend_func=('src_alpha', 'one_minus_src_alpha'))
        self.is_initialized = False
        self.y = None
        self.plot_mode = plot_mode
        self.last_plotted_column = -1
        self.axis_program = None  # Add this line

    def initiateCanvas(self, color=None, index=None, nrows=1, ncols=1, plot_window_sample_count=1000):
        print("Initializing plot canvas...")

        self.n = int(plot_window_sample_count)
        self._reset_data_plot_buffer()

        if color is None:
            color = np.array([0.7, 0.7, 0.7], dtype=np.float32)  # Simple gray color

        # Simple vertex shader for 2D line plotting
        VERT_SHADER = """
        #version 120
        attribute float a_position;
        attribute float a_index;
        uniform float u_scale;
        uniform float u_n;
        void main() {
            float x = -1 + 2*a_index / (u_n-1);
            gl_Position = vec4(x, a_position * u_scale, 0.0, 1.0);
        }
        """

        FRAG_SHADER = """
        #version 120
        uniform vec3 u_color;
        void main() {
            gl_FragColor = vec4(u_color, 1.0);
        }
        """

        self.program = gloo.Program(VERT_SHADER, FRAG_SHADER)
        self.program['a_position'] = self.y
        self.program['a_index'] = np.arange(self.n, dtype=np.float32)
        self.program['u_color'] = color
        self.program['u_scale'] = 1.0
        self.program['u_n'] = self.n

        # Add vertex shader for axis
        AXIS_VERT_SHADER = """
                #version 120
                attribute vec2 a_position;
                void main() {
                    gl_Position = vec4(a_position, 0.0, 1.0);
                }
                """

        AXIS_FRAG_SHADER = """
                #version 120
                void main() {
                    gl_FragColor = vec4(1.0, 1.0, 1.0, 0.5);  // White color with transparency
                }
                """

        # Create vertices for y-axis line and ticks
        axis_vertices = []
        # Main y-axis line
        axis_vertices.extend([(-0.9, -1), (-0.9, 1)])  # Vertical line

        # Add tick marks
        tick_length = 0.05
        for y in np.linspace(-1, 1, 11):  # 11 ticks from -1 to 1
            axis_vertices.extend([
                (-0.9, y),  # Start of tick
                (-0.9 - tick_length, y)  # End of tick
            ])

        self.axis_program = gloo.Program(AXIS_VERT_SHADER, AXIS_FRAG_SHADER)
        self.axis_program['a_position'] = np.array(axis_vertices, dtype=np.float32)

        self.is_initialized = True

    def _reset_data_plot_buffer(self):
        self.y = np.zeros(self.n, dtype=np.float32)
        self.last_plotted_column = -1

    def plot_new_data(self, data_point, next_val=None):
        if self.plot_mode.lower() == 'scrolling':
            self.y[:-1] = self.y[1:]
            self.y[-1] = data_point
        elif self.plot_mode.lower() == 'windowed':
            next_index = self.last_plotted_column + 1
            if next_index >= self.n:
                self._reset_data_plot_buffer()
                next_index = 0
            self.y[next_index] = data_point
            self.last_plotted_column = next_index

        self._update_data()

    def _update_data(self):
        self.program['a_position'].set_data(self.y.astype(np.float32))
        self.update()

    def on_resize(self, event):
        gloo.set_viewport(0, 0, event.physical_size[0], event.physical_size[1])

    def on_draw(self, event):
        if self.is_initialized:
            gloo.clear()
            self.program.draw('line_strip')

    def set_scaling(self, scale):
        if self.is_initialized:
            self.program['u_scale'] = float(scale)

    def on_draw(self, event):
        if self.is_initialized:
            gloo.clear()
            self.program.draw('line_strip')
            # Draw the axis
            self.axis_program.draw('lines')

    def add_y_labels(self):
        # This would require additional text rendering logic
        # You might want to use vispy.scene.Text or another text rendering approach
        pass
