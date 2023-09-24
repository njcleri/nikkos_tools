from pathlib import Path
BASE_PATH = Path(__file__).parent
LINESDF_PATH = (BASE_PATH / "spectrum_tools/linesdf.csv").resolve()

if not LINESDF_PATH.is_file():
    from nikkos_tools.spectrum_tools import line_data
    line_data.make_linesdf(LINESDF_PATH)