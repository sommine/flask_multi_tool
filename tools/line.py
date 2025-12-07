from flask import Blueprint, render_template, request
import plotly.graph_objs as go
import plotly.io as pio

line_bp = Blueprint('line', __name__)

@line_bp.route("/line", methods=["GET", "POST"])
def line():
    equation_text = None
    slope = None
    x_intercept = None
    y_intercept = None
    graph_html = None

    if request.method == "POST":
        try:
            # Get user input
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))

            # Equation text
            equation_text = f"{a}*x + {b} = 0"

            # Calculate slope
            slope = -a  # slope for y = a*x + b ?

            # Calculate intercepts
            y_intercept = b
            x_intercept = -b / a if a != 0 else None

            # Prepare data for graph
            x_vals = [-10, 10]
            y_vals = [a*x + b for x in x_vals]

            # Create Plotly figure
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='y = a*x + b'))
            
            # Plot intercept points
            if y_intercept is not None:
                fig.add_trace(go.Scatter(x=[0], y=[y_intercept], mode='markers+text', name='Y-intercept',
                                         text=[f"({0},{y_intercept})"], textposition="top right"))
            if x_intercept is not None:
                fig.add_trace(go.Scatter(x=[x_intercept], y=[0], mode='markers+text', name='X-intercept',
                                         text=[f"({x_intercept},0)"], textposition="bottom right"))

            fig.update_layout(title="Line Graph", xaxis_title="x", yaxis_title="y", showlegend=True)

            # Convert to HTML
            graph_html = pio.to_html(fig, full_html=False)

        except Exception as e:
            equation_text = f"Error: {e}"

    return render_template("line.html",
                           equation=equation_text,
                           slope=slope,
                           x_intercept=x_intercept,
                           y_intercept=y_intercept,
                           graph_html=graph_html)
