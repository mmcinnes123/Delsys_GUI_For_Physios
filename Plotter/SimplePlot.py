""" Creates a live line plot of IMU euler angle data """

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
        self.y_traces = None
        self.plot_mode = plot_mode
        self.last_plotted_column = -1
        self.axis_program = None
        self.text_program = None

    def initiateCanvas(self, plot_window_sample_count=1000):
        print("Initializing plot canvas...")

        self.n = int(plot_window_sample_count)
        self._reset_data_plot_buffer()

        # Colors for three traces (red, green, blue)
        self.colors = np.array([
            [1.0, 0.0, 0.0],  # Red
            [0.0, 1.0, 0.0],  # Green
            [0.0, 0.0, 1.0],  # Blue
        ], dtype=np.float32)

        VERT_SHADER = """
        #version 120
        attribute float a_position;
        attribute float a_index;
        uniform float u_scale;
        uniform float u_offset;
        uniform float u_n;
        void main() {
            float x = -1 + 2*a_index / (u_n-1);
            // Scale to -180 to 180 range
            float y = (a_position / 180.0);
            gl_Position = vec4(x, y, 0.0, 1.0);
        }
        """

        FRAG_SHADER = """
        #version 120
        uniform vec3 u_color;
        void main() {
            gl_FragColor = vec4(u_color, 1.0);
        }
        """

        # Create three separate programs for three traces
        self.programs = []
        for i in range(3):
            program = gloo.Program(VERT_SHADER, FRAG_SHADER)
            program['a_position'] = self.y_traces[i]
            program['a_index'] = np.arange(self.n, dtype=np.float32)
            program['u_color'] = self.colors[i]
            program['u_scale'] = 1.0
            program['u_offset'] = 0.0
            program['u_n'] = self.n
            self.programs.append(program)

        # Create y-axis and ticks
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
            gl_FragColor = vec4(1.0, 1.0, 1.0, 0.5);
        }
        """

        # Create vertices for y-axis line and ticks
        axis_vertices = []
        # Main y-axis line
        axis_vertices.extend([(-0.9, -1), (-0.9, 1)])  # Vertical line

        # Add tick marks every 20 degrees
        tick_length = 0.05
        for deg in range(-180, 181, 20):
            y = deg / 180.0  # Convert degrees to normalized coordinates
            axis_vertices.extend([
                (-0.9, y),  # Start of tick
                (-0.9 - tick_length, y)  # End of tick
            ])

        self.axis_program = gloo.Program(AXIS_VERT_SHADER, AXIS_FRAG_SHADER)
        self.axis_program['a_position'] = np.array(axis_vertices, dtype=np.float32)

        self.is_initialized = True

    def _reset_data_plot_buffer(self):
        self.y_traces = np.zeros((3, self.n), dtype=np.float32)
        self.last_plotted_column = -1

    def plot_new_data(self, data_points):
        if not isinstance(data_points, np.ndarray) or data_points.shape != (3,):
            raise ValueError("data_points must be a numpy array of shape (3,)")

        if self.plot_mode.lower() == 'scrolling':
            self.y_traces[:, :-1] = self.y_traces[:, 1:]
            self.y_traces[:, -1] = data_points
        elif self.plot_mode.lower() == 'windowed':
            next_index = self.last_plotted_column + 1
            if next_index >= self.n:
                self._reset_data_plot_buffer()
                next_index = 0
            self.y_traces[:, next_index] = data_points
            self.last_plotted_column = next_index

        self._update_data()

    def _update_data(self):
        for i, program in enumerate(self.programs):
            program['a_position'].set_data(self.y_traces[i].astype(np.float32))
        self.update()

    def on_resize(self, event):
        gloo.set_viewport(0, 0, event.physical_size[0], event.physical_size[1])

    def on_draw(self, event):
        if self.is_initialized:
            gloo.clear()
            # Draw the axis first
            self.axis_program.draw('lines')
            # Then draw all three traces
            for program in self.programs:
                program.draw('line_strip')