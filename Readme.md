## Russian Troll Detector

This project classifies Russian Fake News Trolls and Normal News Tweets, identifying the difference between them using the Russian "troll factory" twitter dataset.

### Project Files

- results.ipynb
    + Start here.  Why I chose Albert, findings, and looking forward.
- convert_dataset.ipynb
    + Code used to convert the Russian "troll factory" twitter dataset and the Twitter Stream dataset into the train dev test tsv format Albert expects.
- make_vocab.ipynb
    + Code used to make vocabulary file for training.
- albert_train.ipynb
    + Final notebook.  Successful Albert training and findings.
- bert_old.ipynb
    + Scrapped Bert notebook.  I tried to use Bert, but had vram issues.
- albert_old.ipynb
    + Scrapped Albert notebook.  Running Albert within a jupyter notebook takes up too much resources on the TX2.
- plot_helper.py
    + Contains functions to plot data, so results.ipynb is not flooded with code.
- ALBERT/
    + A clone of the Albert repo found at https://github.com/google-research/ALBERT
    + Modified for TX2 support.
- data/
    + Datasets downloaded and processed temp files.
- model/
    + Pre-trained Albert base model and vocabulary.
    + Downloaded from https://tfhub.dev/google/albert_base/3
- out/
    + Albert training, validation, and testing files are saved her.