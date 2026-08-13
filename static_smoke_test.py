import ast
from pathlib import Path

source = Path("app.py").read_text(encoding="utf-8")
tree = ast.parse(source)
imports = {node.names[0].name for node in tree.body if isinstance(node, ast.Import) and node.names}
assert "os" in imports
assert all(not (isinstance(node, ast.ImportFrom) and node.module in {"diffusers", "qwenimage.pipeline_qwenimage_edit_plus", "qwenimage.transformer_qwenimage"}) for node in tree.body)
function_names = {node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
assert "get_pipeline" in function_names
assert "clear_memory" in function_names
assert "_pipe = None" in source
print("FIRERED_STATIC_LAZY_LOAD_CHECK_OK")
