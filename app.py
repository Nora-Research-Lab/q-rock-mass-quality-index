import gradio as gr
from q_rock_mass_quality_index import compute_q, classify_q, support_recommendation

def calculate_q_rqd(rqd, jn, jr, ja, jw, srf, span):
    jn_val = {"Massive, no or few joints": 0.5, "One joint set": 1.0, "Two joint sets": 2.0,
              "Three joint sets": 3.0, "Four or more joint sets": 4.0, "Crushed rock, earthlike": 5.0}.get(jn, 1.0)
    jr_val = {"Discontinuous joints": 4.0, "Rough or irregular, undulating": 3.0,
              "Smooth, undulating": 2.5, "Filled or healed": 2.0,
              "Rough, planar": 1.5, "Smooth, planar": 1.0, "Slickensided, planar": 0.5}.get(jr, 1.0)
    ja_val = {"Tightly healed, hard, non-softening": 0.75, "Unweathered, surface staining only": 1.0,
              "Slightly altered": 2.0, "Moderately altered": 4.0,
              "Highly altered": 6.0, "Soft clay coatings": 8.0, "Swelling clay": 10.0}.get(ja, 1.0)
    jw_val = {"Dry excavations or minor inflow": 1.0, "Damp (water seepage)": 0.66,
              "Wet (water inflow)": 0.5, "Medium inflow": 0.33, "High inflow": 0.2}.get(jw, 1.0)
    srf_val = {"Low stress, near surface": 0.5, "Medium stress": 1.0, "High stress": 2.0,
               "Very high stress": 4.0, "Extremely high stress": 8.0}.get(srf, 1.0)

    q = compute_q(rqd, jn_val, jr_val, ja_val, jw_val, srf_val)
    cls = classify_q(q)
    rec = support_recommendation(q, span)

    # Build color bar HTML (log scale from 0.001 to 1000)
    log_q = -3.0
    if q > 0:
        log_q = max(-3.0, min(3.0, __import__('math').log10(q)))
    pos = (log_q + 3.0) / 6.0 * 100  # percentage
    bar_html = f"""
    <div style="width:100%; height:30px; background: linear-gradient(to right, red, yellow, green, cyan, blue); border:1px solid #333; position:relative;">
        <div style="position:absolute; left:{pos}%; top:-5px; width:0; height:0; border-left:8px solid transparent; border-right:8px solid transparent; border-bottom:10px solid black;"></div>
    </div>
    <div style="display:flex; justify-content:space-between; font-size:10px; margin-top:2px;">
        <span>0.001</span><span>0.01</span><span>0.1</span><span>1</span><span>10</span><span>100</span><span>1000</span>
    </div>
    """
    return f"<h2 style='font-size:2em;'>{q:.4f}</h2>", cls, bar_html, rec

with gr.Blocks(title="Q-Rock Mass Quality Index") as demo:
    gr.Markdown("# Q-Rock Mass Quality Index (Barton et al., 1974)")
    with gr.Row():
        with gr.Column(scale=1):
            rqd = gr.Slider(0, 100, value=75, label="RQD (%)")
            jn = gr.Dropdown(choices=["Massive, no or few joints", "One joint set", "Two joint sets",
                                       "Three joint sets", "Four or more joint sets", "Crushed rock, earthlike"],
                             value="Two joint sets", label="Jn (Joint Set Number)")
            jr = gr.Dropdown(choices=["Discontinuous joints", "Rough or irregular, undulating",
                                       "Smooth, undulating", "Filled or healed", "Rough, planar",
                                       "Smooth, planar", "Slickensided, planar"],
                             value="Rough or irregular, undulating", label="Jr (Joint Roughness Number)")
            ja = gr.Dropdown(choices=["Tightly healed, hard, non-softening", "Unweathered, surface staining only",
                                       "Slightly altered", "Moderately altered", "Highly altered",
                                       "Soft clay coatings", "Swelling clay"],
                             value="Unweathered, surface staining only", label="Ja (Joint Alteration Number)")
            jw = gr.Dropdown(choices=["Dry excavations or minor inflow", "Damp (water seepage)",
                                       "Wet (water inflow)", "Medium inflow", "High inflow"],
                             value="Dry excavations or minor inflow", label="Jw (Joint Water Reduction)")
            srf = gr.Dropdown(choices=["Low stress, near surface", "Medium stress", "High stress",
                                       "Very high stress", "Extremely high stress"],
                              value="Medium stress", label="SRF (Stress Reduction Factor)")
            span = gr.Number(value=8, label="Tunnel Span (m)")
            btn = gr.Button("Calculate", variant="primary")
        with gr.Column(scale=1):
            q_val = gr.HTML(label="Q-Value")
            q_class = gr.Textbox(label="Rock Mass Class")
            q_bar = gr.HTML(label="Q-Scale")
            support = gr.Textbox(label="Recommended Support")

    btn.click(fn=calculate_q_rqd,
              inputs=[rqd, jn, jr, ja, jw, srf, span],
              outputs=[q_val, q_class, q_bar, support])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
