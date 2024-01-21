# Segmentation for Liujgoj Cantonese
This is a segmentation for Liujgoj Cantonese(Yvthyvq).  呢個係粵語分詞器，適用於粵語嘅溜歌版本。

1，本分詞器split_words.py嘅目的係用於詞典嘅製作。

* 對性名進行咗前綴、中綴嘅去除；
* 時態嘅處理採用白名單製aspect.txt，比如：“yukhganr(肉緊)”嘅"ganr"唔係時態，唔作去除；
* 對複合詞“pukj-neiq-go-gaaij（仆你個街）”等進行直接合併爲“pukjgaaij(仆街)”；
* 個別詞提前處理，比如：“zip-gwaan-saangj(接慣生)”， “bin-ganr(變緊)”；
* 普通話同粵語嘅混合詞語唔處理，比如：“开玩笑-zor”自動被分爲“开玩笑”同"-zor";
* 最後得到嘅結果喺4.xlsx度。


2，分詞器simple.py, 按照除了缩写符号（撇號"'"）和连字符号"-"以外的其它标点符号以及空格嚟划分单词。 用於教學同AI訓練。

* 含有縮寫符號" ' "。 比如：“hor' mxhoryiq(可唔可以)”中嘅“hor'”代表“horyiq”嘅縮寫； “'deih”代表"keoiqdeih"嘅縮寫；
* 含有連字符"-"嘅複合詞；比如： "cungjzor-loengx(沖咗涼)"， "pukj-neiq-go-gaaij(仆你個街)"；
* 含有英語。比如： "I'm";
* 含有普通話。比如： "开玩笑-zor"。"开玩笑"發普通話音，"-zor"發粵語音，表示完成態。
* 含有字母同數字。比如： "AK47", "7-11"。
* 最後嘅結果放喺： 簡單分詞同詞頻.xlsx度。

* 修改說明：而家對粵語嘅時態有咗唔同嘅認識，認爲粵語只有進行態“ganr”同完成態“zor”兩種。而且對“結婚”，“離婚”同“沖涼”等單詞作詞組處理。所以對單詞庫作出調整。