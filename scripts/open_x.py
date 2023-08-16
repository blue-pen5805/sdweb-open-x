import gradio as gr
import modules.scripts as scripts

class Script(scripts.Script):
    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def after_component(self, component, **kwargs):
         if kwargs.get("elem_id") == "extras_tab":
            gr.Button(value="X", elem_id="open_x")

    def ui(self, is_img2img):
        return
