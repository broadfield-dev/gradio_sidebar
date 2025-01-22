# gradio_sidebar
Python module to add 3 optional sidebars (top, left, right) that will contain gradio elements.

## How to use it

## 1. Install
```python
git clone https://github.com/broadfield-dev/gradio_sidebar.git
```

## 2.1 Run
Import and call the hooks from the 'gs' alias 

```python
import gradio as gr
import gradio_sidebar.gradio_sidebar as gs

#set the head and css to gs.head and gs.css
with gr.Blocks( head = gs.head, css=gs.css ) as app:
    # These 3 hooks provide the clickable tabs to open the corresponding sidebar
    gr.HTML(gs.leftbar)  #ON
    gr.HTML(gs.rightbar)  #ON
    #gr.HTML(gs.topbar)  #OFF
```
## 2.2 Run
Add the appropriate 'elem_id=' tag a Gradio Group and it will become the sidebar containing the items within the Group

```python
  with gr.Group(elem_id="gs_top_control_panel"):
      gr.Textbox()
      gr.Slider()
      gr.Image()
  with gr.Group(elem_id="gs_left_control_panel"):
      gr.Textbox()
      gr.Slider()
      gr.Image()
  with gr.Group(elem_id="gs_right_control_panel"):
      gr.Textbox()
      gr.Slider()
      gr.Image()
  gr.Chatbot()
  gr.Textbox()
  gr.Image()
``` 
