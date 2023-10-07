import subprocess

themes = { "core": 
      [ "AnnArbor", "Antibes", "Berkeley", "Berlin", "Bergen", "Boadilla",
        "Copenhagen", "Darmstadt", "Dresden", "EastLansing", "Frankfurt",
        "Goettingen", "Hannover", "Ilmenau", "JuanLesPins", "Luebeck",
        "Malmoe", "Madrid", "Marburg", "Montpellier", "PaloAlto",
        "Pittsburgh", "Rochester", "Singapore", "Szeged", "Warsaw",
        "CambridgeUS", "default", "boxes"
      ],
  "font": 
      [
        "default", "serif", "structurebold", "structureitalicserif",
        "structuresmallcapsserif"
      ],
  "color":
      [
        "default", "crane", "albatross", "seahorse", "whale", "dolphin",
        "rose", "orchid", "sidebartab", "lily", "structure", "dove", "seagull",
        "beetle", "fly", "wolverine", "spruce", "beaver", "monarca",
        "albatrossstylish" # This is a special case: see the .tex file
      ],
  "outer":
      [
        "default", "infolines", "miniframes", "shadow", "sidebar",
        "smoothbars", "smoothtree", "split", "tree"
      ],
  "inner": ["default", "circles", "rectangles", "rounded", "inmargin"]
}

for type, themelist in themes.items():
  themetype = ""
  if(type != "core"):
    themetype = type
  tex_file_name = "beamer" + themetype + "themeexample.tex"
  for themelist_item in themelist:
    # subprocess.run(["pdflatex", "\\def\\themename{" + f"{themelist_item}" + "}", f"\\input {tex_file_name}"])
    # subprocess.run(["mv", f"beamer{themetype}themeexample.pdf", f"beamerug{themetype}theme{themelist_item}.pdf"])
    subprocess.run(["pdftocairo", "-svg", "-o", f"beamerug{themetype}theme{themelist_item}.pdf", f"beamerug{themetype}theme{themelist_item}-page1.svg"])
    subprocess.run(["pdftocairo", "-svg", "-e", f"beamerug{themetype}theme{themelist_item}.pdf", f"beamerug{themetype}theme{themelist_item}-page2.svg"])


print("Conversion finished.")
