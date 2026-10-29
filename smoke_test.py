import os

os.environ.setdefault("GRADIO_ANALYTICS_ENABLED", "False")

import app

assert app.device.type in {"cpu", "cuda"}
assert app._pipe is None, "El modelo no debe cargarse durante la importación"
assert app.update_dimensions_on_upload(None) == (1024, 1024)
print("FIRERED_LAZY_IMPORT_SMOKE_OK")
print(f"DEVICE={app.device.type}")
