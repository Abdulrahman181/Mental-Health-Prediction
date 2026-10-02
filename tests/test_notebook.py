import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "Mental Health Prediction.ipynb"


class NotebookIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with NOTEBOOK.open(encoding="utf-8") as handle:
            cls.notebook = json.load(handle)

    def test_notebook_uses_nbformat_four(self):
        self.assertEqual(self.notebook.get("nbformat"), 4)
        self.assertIsInstance(self.notebook.get("cells"), list)

    def test_code_cells_are_valid_python(self):
        code_cells = [
            cell for cell in self.notebook["cells"] if cell.get("cell_type") == "code"
        ]
        self.assertTrue(code_cells)
        for index, cell in enumerate(code_cells):
            source = "".join(cell.get("source", []))
            with self.subTest(cell=index):
                compile(source, f"notebook-cell-{index}", "exec")

    def test_cached_outputs_are_cleared(self):
        for index, cell in enumerate(self.notebook["cells"]):
            if cell.get("cell_type") == "code":
                with self.subTest(cell=index):
                    self.assertEqual(cell.get("outputs", []), [])
                    self.assertIsNone(cell.get("execution_count"))


if __name__ == "__main__":
    unittest.main()
