from flask import Blueprint, render_template, request
import plotly.graph_objs as go
import plotly.io as pio
import math

parabolic_bp = Blueprint('parabolic', __name__)

@parabolic_bp.route("/parabolic", methods=["GET", "POST"])
def parabolic():
    equation = None
    discriminant = None
    x1 = None
    x2 = None
    vertex_x = None
    vertex_y = None
    graph_html = None

    if request.method == "POST":
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            c = float(request.form.get("c"))

            equation = f"{a}x² + {b}x + {c} = 0"

            if a == 0:
                equation = "❌ Not a quadratic function (a cannot be 0)"
                return render_template("parabolic.html", equation=equation)

            # ───────── Compute math ─────────
            discriminant = b*b - 4*a*c

            # Vertex
            vertex_x = -b / (2*a)
            vertex_y = a*vertex_x**2 + b*vertex_x + c

            # Roots
            if discriminant > 0:
                sqrtD = math.sqrt(discriminant)
                x1 = (-b + sqrtD) / (2*a)
                x2 = (-b - sqrtD) / (2*a)
            elif discriminant == 0:
                x1 = x2 = -b / (2*a)
            else:
                x1 = x2 = None  # no real roots

            # ───────── Make Graph ─────────
            x_vals = [vertex_x + i for i in [x/10 for x in range(-200, 201)]]
            y_vals = [a*x*x + b*x + c for x in x_vals]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode="lines", name="Parabola"))

            # Plot real roots
            if x1 is not None:
                fig.add_trace(go.Scatter(x=[x1], y=[0], mode="markers+text",
                                        name="Root 1",
                                        text=[f"({x1:.2f},0)"],
                                        textposition="bottom center"))
            if x2 is not None and x2 != x1:
                fig.add_trace(go.Scatter(x=[x2], y=[0], mode="markers+text",
                                        name="Root 2",
                                        text=[f"({x2:.2f},0)"],
                                        textposition="bottom center"))

            # Plot vertex
            fig.add_trace(go.Scatter(x=[vertex_x], y=[vertex_y], mode="markers+text",
                                    name="Vertex",
                                    text=[f"({vertex_x:.2f},{vertex_y:.2f})"],
                                    textposition="top center"))

            fig.update_layout(
                title="Quadratic Function",
                xaxis_title="x",
                yaxis_title="y",
                showlegend=True
            )

            graph_html = pio.to_html(fig, full_html=False)

        except Exception as e:
            equation = f"Error: {e}"

    return render_template("parabolic.html",
                           equation=equation,
                           discriminant=discriminant,
                           x1=x1,
                           x2=x2,
                           vertex_x=vertex_x,
                           vertex_y=vertex_y,
                           graph_html=graph_html)
