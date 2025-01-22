import gradio as gr
import gradio_sidebar as gs

with gr.Blocks(head=gs.head,css=gs.css) as app:
    gr.HTML(gs.topbar)
    gr.HTML(gs.leftbar)
    gr.HTML(gs.rightbar)
    with gr.Group(elem_id="gs_top_control_panel"):
        gr.Textbox()
        gr.Slider()
        gr.Image()
    with gr.Group(elem_id="gs_left_control_panel"):
        gr.Textbox()
        gr.Textbox()
        gr.Textbox()
        gr.Textbox()
        gr.Slider()
        gr.Image()
    with gr.Group(elem_id="gs_right_control_panel"):
        gr.Textbox()
        gr.Textbox()
        gr.Textbox()
        gr.Textbox()
        gr.Slider()
        gr.Image()
    gr.Chatbot()
    gr.Textbox()
    gr.Image()
    gr.Image()
        
app.launch()
