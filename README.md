# mnist-for-decoration-font

## about

* mnist @ python
* is recognize for decoration font by mnist? test repository
* decoration font made by @irimo (auto-font-margin)
* tensorflow's version is newest

## usage

### prepare

```
$ [cd repository_root at host PC]
$ docker build . -t mnist-for-decoration-font
$ docker run -it -v $(pwd)/:/home mnist-for-decoration-font
```

### predict strange font(disableTT)

```
$ python3 convert_font_to_npy.py
$ python3 predict.py
```

### 言い訳

* 手描きフォントを認識してくれるmnist、自作のデコレーションフォントは認識するんだろうかと試しました
* 結果は2と5だけ認識してくれてうれしいですが、それ以外はご認識してしまったのでこのテストはここで終わり。人類に私のデコレーションフォントの認識は早かった...!と思っていますが、自由にいじっていただいてちゃんと認識したらPRとか送っていただければ嬉しきです。