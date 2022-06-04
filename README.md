# mnist-for-decoration-font

## about

* mnist @ python
* is recognize for decoration font by mnist? test repository
* decoration font made by @irimo (auto-font-margin)
* tensorflow's version is newest

## usage

```
$ [cd repository_root at host PC]
$ docker build . -t mnist-for-decoration-font
$ docker run -it -v $(pwd)/:/home mnist-for-decoration-font
$ python3 convert_decoration_font.py
$ python3 predict.py
```