
# python scripts/app.py

from txt2img import generate_image_by_text
import os
import shutil

import matplotlib.pyplot as plt


class App(object):
    def __init__(self, text, save_fig=True):
        self.text = text
        self.save_fig = save_fig
        self.seed = 42

    def run(self):
        opt = generate_image_by_text(self.text)
        img = plt.imread(os.path.join(opt.outdir, 'samples', '00000.png'))
        plt.imshow(img)
        plt.xticks([])
        plt.yticks([])
        plt.title(self.text)
        plt.show()
        if not self.save_fig:
            shutil.rmtree(opt.outdir)


if __name__ == "__main__":
    app = App('Empty talk would lead a country astray,and hard work can revitalize a nation.')
    app.run()
