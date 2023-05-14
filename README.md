# Segmentation for Liujgoj Cantonese
This is a segmentation for Liujgoj Cantonese(Yvthyvq).  呢個係粵語分詞器，適用於粵語嘅溜歌版本。
本分詞器嘅目的係用於詞典嘅製作。
* 對單詞進行咗前綴、中綴同後綴嘅去除；
* 時態嘅處理採用白名單製，比如：“yukhganr(肉緊)”嘅"ganr"唔係時態，唔作去除；
* 對離合詞“pukj-neiq-go-gaaij（仆你個街）”進行直接合併爲“pukjgaaij(仆街)”；
* 個別詞提前處理，比如：“zip-gwaan-saangj(接慣生)”， “bin-ganr(變緊)”；
* 普通話同粵語嘅混合詞語單獨處理，比如：“开玩笑-zor”還原爲“开玩笑”。
