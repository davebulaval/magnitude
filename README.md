# Magnitude fork that only supports Word2Vec, GloVe and fastText embeddings
> I've forked the [other lite version](https://github.com/neuml/magnitude) since package naming was bad and was sometime mixup with the original one

This repository makes the following changes to the excellent Magnitude project: 

- Project simplified to only support Word2Vec, GloVe and fastText embeddings
- Approximate indexing/search methods removed
- Annoy, AllenNLP (ELMo) and Torch dependencies removed
- Removed internal SQLite related libraries (pysqlite, apsw) and use system SQLite package
- Removed logic to download and stream models. Models must all be locally available, remote servers will not be checked.
- Build process simplified to use PyPi dependencies

See Magnitude project for documentation and links to pre-trained models: https://github.com/plasticityai/magnitude
