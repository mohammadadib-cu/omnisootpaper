from pathlib import Path
import os

src_path = Path("");
allbib_path = src_path/Path("all.bib");
allbib_content = [];

if allbib_path.exists():
    os.remove(allbib_path);

for file_path in src_path.glob("**/*.bib"):
    if file_path.name.startswith("_ref"):
        print(f"{file_path.name} is added to all.bib");
        allbib_content += [file_path.read_text(encoding="utf8")];
    
allbib_path.write_text("\n".join(allbib_content), encoding="utf-8");