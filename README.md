参照：main_music_player_ver_0_12.py

今回の製品では、主に7つの機能を付けた。以下の通りである。
1.	カメラによる顔認識→集中力の測定
2.	適した音楽のダウンロード機能
3.	音楽再生機能
4.	超音波センサによる、スマートフォンを置いたことの検出機能。
5.	ライトの自動的な点灯・消灯
6.	モーターによるライト部分の可動。
7.	ラインAPIを用いた勉強時間の通知。

(3)	要求される働き
　要求される働きについて、先ほど挙げた7つの機能ごとに説明していく。

(3)-(1) - カメラによる顔認識→集中力の測定
今回の製品では、音楽の再生時に、ユーザーの集中度に応じて、プレイリストを変更するという必要があった。そこで今回は、カメラによる顔認識プログラムを用いて、集中度を測定するということを行った。
　
　上に示したのが、この機能の動作概要図である。以上のような構造をとることによって、最低限の処理の重さで、簡単に安定した測定を行うことが出来た。
　方法は至極単純で、カメラが正面に向いたの顔を判定したら、内部に保持する集中度スコアを下げ、逆に判定しなかったら、スコアを上げるというものになっている。勉強や作業中に正面を向き、カメラと向き合うことはない、ということを仮定している。

　本来であれば、姿勢推定などの、より正確な測定方法を使用するべきかもしれなかったが、カメラ位置がデザイン上でどこに設置されるのかが試行錯誤で不明であるという点や、ラズベリーパイに負担になるような処理をできるだけさせたくない、他の機能の拡充を行いたいという理由で、今回はこの手法を取った。

(3)-(2) 適した音楽のダウンロード機能
　勉強や作業に適した音楽を流すために、大手音楽配信サイトであるSpotifyと、大手動画配信サービスのYouTubeのAPIを利用して、システムを構築した。以下がその流れ図である。

　まず、ユーザーが、勉強や作業をする際に、どのような音楽を聴きたいのかを、音楽のジャンルや、曲名などを入力することで、その音楽をダウンロードすることができる。その際に、ユーザーが入力した情報を、SpotifyのAPIに送信することで、その情報に合致する音楽を検索することができる。そして、その検索結果を、YouTubeのAPIに送信することで、その音楽のURLを取得することができる。そして、そのURLを、YouTube-dlというライブラリを用いて、音楽ファイルとしてダウンロードすることができる。そして、その音楽ファイルを、音楽再生機能で再生することができる。

　このような流れをとることで、ユーザーが、勉強や作業をする際に、どのような音楽を聴きたいのかを、音楽のジャンルや、曲名などを入力することで、その音楽をダウンロードすることができる。

(3)-(3) 音楽再生機能
　音楽再生機能は、先ほど説明した、適した音楽のダウンロード機能でダウンロードした音楽を再生する機能である。
　この機能では、pythonファイルの書き換えによって、そのままの再生と、シャッフル再生を変更することができる。スマホを置いたときに、再生され、スマホを離したときに、再生が停止するという機能も実装した。
    
(3)-(4) 超音波センサによる、スマートフォンを置いたことの検出機能。
　スマートフォンを置いたことを検出するために、超音波センサを用いた。以下がその流れ図である。

　まず、超音波センサから、超音波が発射され、それが反射して、センサに戻ってくるまでの時間を計測する。そして、その時間を、音速を用いて、距離に変換する。そして、その距離が、一定の距離よりも短い場合、スマートフォンが置かれたと判断する。そして、スマートフォンが置かれたと判断した場合、ライトを点灯させる。今回はその距離を10cmとした。

(3)-(5) ライトの自動的な点灯・消灯

　ライトの自動的な点灯・消灯は、先ほど説明した、超音波センサによる、スマートフォンを置いたことの検出機能を用いて実装した。以下がその流れ図である。

(3)-(6) モーターによるライト部分の可動。

　モーターによるライト部分の可動は、先ほど説明した、超音波センサによる、スマートフォンを置いたことの検出機能を用いて、実装した。以下がその流れ図である。
    
(3)-(7) ラインAPIを用いた勉強時間の通知。

　ラインAPIを用いた勉強時間の通知は、以下の流れ図である。

　今回は、ユーザがスマートフォンを置き、離したことを検出した際に、ラインに通知を送るという形で、勉強時間の通知を行った。ラインに通知を送るために、ラインのAPIを用いた。ラインのAPIを用いることで、ラインに通知を送ることができる。ラインに通知を送ることで、ユーザーは、勉強時間を把握することができる。

(4)	保証すべき項目とレベル、その理由

    　今回の製品では、以下の項目を保証すべき項目とした。
    
(4)-(1) 音楽再生機能

　音楽再生機能は、今回の製品の中で、最も重要な機能である。なぜなら、音楽再生機能がなければ、ユーザーは、勉強や作業をする際に、音楽を聴くことができないからである。そのため、音楽再生機能は、必ず保証すべき項目である。

(4)-(2) 適した音楽のダウンロード機能

　適した音楽のダウンロード機能は、今回の製品の中で、2番目に重要な機能である。なぜなら、適した音楽のダウンロード機能がなければ、ユーザーは、勉強や作業をする際に、適した音楽を聴くことができないからである。そのため、適した音楽のダウンロード機能は、必ず保証すべき項目である。

(4)-(3) ラインAPIを用いた勉強時間の通知。

　ラインAPIを用いた勉強時間の通知は、今回の製品の中で、3番目に重要な機能である。なぜなら、ラインAPIを用いた勉強時間の通知がなければ、ユーザーは、勉強や作業をする際に、勉強時間を把握することができないからである。そのため、ラインAPIを用いた勉強時間の通知は、必ず保証すべき項目である。

(4)-(4) カメラによる顔認識→集中力の測定

　カメラによる顔認識→集中力の測定は、今回の製品の中で、4番目に重要な機能である。なぜなら、カメラによる顔認識→集中力の測定がなければ、ユーザーは、勉強や作業をする際に、集中力を把握することができないからである。そのため、カメラによる顔認識→集中力の測定は、必ず保証すべき項目である。

(4)-(5) 超音波センサによる、スマートフォンを置いたことの検出機能。

　超音波センサによる、スマートフォンを置いたことの検出機能は、今回の製品の中で、5番目に重要な機能である。なぜなら、超音波センサによる、スマートフォンを置いたことの検出機能がなければ、ユーザーは、勉強や作業をする際に、スマートフォンを置いたことを検出することができないからである。そのため、超音波センサによる、スマートフォンを置いたことの検出機能は、必ず保証すべき項目である。
    
(4)-(6) ライトの自動的な点灯・消灯

　ライトの自動的な点灯・消灯は、今回の製品の中で、6番目に重要な機能である。なぜなら、ライトの自動的な点灯・消灯がなければ、ユーザーは、勉強や作業をする際に、ライトの自動的な点灯・消灯を行うことができないからである。そのため、ライトの自動的な点灯・消灯は、必ず保証すべき項目である。   

(4)-(7) モーターによるライト部分の可動。

　モーターによるライト部分の可動は、今回の製品の中で、7番目に重要な機能である。なぜなら、モーターによるライト部分の可動がなければ、ユーザーは、勉強や作業をする際に、モーターによるライト部分の可動を行うことができないからである。そのため、モーターによるライト部分の可動は、必ず保証すべき項目である。   
    
(5)	設計根拠（含：設計式と設計値、安全率、フローチャート（プログラム）、実験結果、引用技術方式、従来例など)
    
(5)-(1) 音楽再生機能

    　音楽再生機能は、以下のようなプログラムで実装した。
    
    ```python
    (省略)
    ```

(5)-(2) 適した音楽のダウンロード機能

    　適した音楽のダウンロード機能は、以下のようなプログラムで実装した。
    
    ```python
    (省略)
    ```

(5)-(3) ラインAPIを用いた勉強時間の通知。

    　ラインAPIを用いた勉強時間の通知は、以下のようなプログラムで実装した。
    
    ```python
    (省略)
    ```

(5)-(4) カメラによる顔認識→集中力の測定

    　カメラによる顔認識→集中力の測定は、以下のようなプログラムで実装した。
    
    ```python
    (省略)
    ```

(5)-(5) 超音波センサによる、スマートフォンを置いたことの検出機能。

    　超音波センサによる、スマートフォンを置いたことの検出機能は、以下のようなプログラムで実装した。
    
    ```python
    (省略)
    ```

(5)-(6) ライトの自動的な点灯・消灯

    　ライトの自動的な点灯・消灯は、以下のようなプログラムで実装した。
    
    ```python
    (省略)
    ```

(5)-(7) モーターによるライト部分の可動。

    　モーターによるライト部分の可動は、以下のようなプログラム  で実装した。
    
    ```python
    (省略)
    ```         

(6)	確認すべき項目（試作で確認すべき項目と判定基準及び測定方法）

(6)-(1) 音楽再生機能

(6)-(2) 


(7)	試作後の確認結果


(8)	参考文献

