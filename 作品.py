# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:18:01 2021

@author: sakii
"""

import streamlit as st
st.title("DAREKA-ATEMASHU")
st.write("心理テストへようこそ！")

option=st.selectbox(
    "Q1. プライベート空間である寝室の写真。どんなジャンルの写真を飾りますか？　選んだもので、あなたが今、好きな人にしてもらいたいと思っていることがわかります。",
    list(["ペットの写真","お料理の写真","大自然の写真","乗り物の写真",])
    )
"あなたが選択したのは、",option,"です。"

if option == "ペットの写真":
    st.write("1. ペットの写真を選んだあなたの望みは「自分のことを見てほしい」ペットの写真は「自己愛」を意味しています。あなたは今、気になる人や付き合っている人に「自分のことを見てほしい」と思っているようです。たとえば恋人から深く愛されていないと感じているのかもしれません。あるいは片思いの相手に、もう少し気にしてほしいと願っているのでしょうか……。ただ、気がつかないうちにコミュニケーションが取れていない恐れもあります。心当たりがないという人も、自分から話をしたり、プレゼントを贈ったりして、あなたの存在をアピールしてみましょう。")
if option == "お料理の写真":
    st.write("2. お料理の写真を選んだあなたの望みは「悩みを聞いてほしい」お料理の写真は「逃避」を意味しています。あなたは今、気になる人や付き合っている人に「悩みを聞いてほしい」と思っているようです。たとえば恋人に仕事での責任のプレッシャーについて聞いてほしいのかもしれません。あるいは片思いの相手にちょっとした悩みを相談してみたいのでしょうか……。ただ、あなた自身気づかないうちに心配をかけまいと周囲を避けている恐れもあります。心当たりがなくても、時間をつくって信頼できる人に相談するとよいでしょう。きっと答えがでるはずです。")
if option == "大自然の写真":
    st.write("3. 大自然の写真を選んだあなたの望みは「自分のことは放っておいてほしい」大自然の写真は「孤高」を意味しています。あなたは今、気になる人や付き合っている人に「自分のことは放っておいてほしい」と思っているようです。たとえば恋人からしつこくされたりするのにうんざりしているのかもしれません。あるいは片思いの相手に、媚びた態度をとってしまったことを後悔しているのでしょうか……。ただ、あなた自身、気がつかないうちに何もかもに対して頑張りすぎて疲れている恐れもあります。たとえ心当たりがなくても、休めるときには休むように心がけましょう。")
if option == "乗り物の写真":
    st.write("4. 乗り物の写真を選んだあなたの望みは「信じてついてきてほしい」乗り物の写真は「独立心」を意味しています。あなたは今、気になる人や付き合っている人に「信じてついてきてほしい」と思っているようです。たとえば恋人に裏切られたと感じる出来事があったのかもしれません。あるいは片思いの相手にもう一歩踏み込んで気持ちを表明したいと願っているのでしょうか……。ただ、気づかないうちに自分のことで手一杯になり、他人の意見を聞けなくなっている恐れもあります。たとえ心当たりがなくても、自分の状態を周りに話して、アドバイスをもらいましょう。")


st.write("Q2. 選んだ色でわかる！あなたの「プライドの高さ」")
from PIL import Image 
img=Image.open("プライドの高さ.png")
st.image(img,caption="色",use_column_width=True)

option_1=st.selectbox(
    "この中であなたが好きな色はどれですか？次から一番近いものを選んでください",
    list(["A : ラベンダー","B : ロイヤルブルー","C : オフホワイト","D : ランプブラック",])
    )
"あなたが選択したのは、",option_1,"です。"

if option_1 == "A : ラベンダー":
    st.write("A：「ラベンダー」を選んだあなた…プライドの高さ40％。あなたは、好きなことなら一生懸命エネルギーを注ぐタイプでしょう。でも、自分が前に出ることを好まず、誰かのサポートに回ることも少なくありません。そんなあなたなので、こだわるところはこだわるのですが、そうでない部分はどうでもいいと感じるはず。本当はもう少しうぬぼれてもいいのに、相手に譲ってしまうところがあるのでは？自分をアピールすることも、時には必要なことだと意識しましょう。そうすれば、あなたの魅力はさらに輝くはず。")
if option_1 == "B : ロイヤルブルー":
    st.write("B：「ロイヤルブルー」を選んだあなた…プライドの高さ95％。あなたのプライドの高さは、相当なもの。傍から見ると、少し“高飛車”のように見られるかもしれません。人に媚びず自分の力で物事を成していこうとする姿は、周囲から見ると憧れられる存在でしょう。しかし、その高すぎるプライドゆえに、深く関わる相手への当たりが厳しく、プライベートでは素直になれないところが。リーダーとしては優れていますがが、もう少し周りに優しくしないと、親しい人ほど敬遠されてしまう可能性も…。")
if option_1 == "C : オフホワイト":
    st.write("C：「オフホワイト」を選んだあなた…プライドの高さ20％。あなたのプライドはかなり低く、プライドよりも周囲との関係性重視かもしれません。いつも低姿勢で、問題があればすぐに謝る姿勢は、好感が持てる反面、どこか頼りなく見えるところが。悪くもないのに謝りすぎると、逆に“卑屈な人”とのレッテルを貼られる場合もあります。謙虚な姿勢はそのままに、自分の意見をはっきり言えるように努力してみましょう。そうすれば、人気や好感度がどんどん高まっていくはず。")
if option_1 == "D : ランプブラック":
    st.write("D：「ランプブラック」を選んだあなた…プライドの高さ60％。あなたは、わりと自信家のようですが、それを表に出さない賢いタイプ。人当たりは良いのですが、いざというときは頼りになるところも持ち合わせている…それはあなたが自分を否定されたくないという思いの強さから。自分に自信はあるけど、それを人には強要しない。まさに、ちょうどいいバランスのプライドの持ち主。人間関係も恋愛も上手くいくタイプだと言えます。ただ、心の中での葛藤は多いかもしれません。")


option_2=st.selectbox(
    "Q3. どの食べ物が好きですか？次の4つから1つを選んでください。",
    list(["A : 舌が焼けつくような辛いもの","B : 体にやさしい緑黄色野菜","C : 甘いもの大好き！お菓子","D : 生きる糧！肉！肉！肉！",])
    )
"あなたが選択したのは、",option_2,"です。"

if option_2 == "A : 舌が焼けつくような辛いもの":
    st.write("心身ともに強く、柔軟な発想ができるチャレンジャーです。どんな状況でも適切に対処する準備ができています。ジェットコースターのような毎日を熱望しており、自ら危険を犯すこともしばしば。")
if option_2 == "B : 体にやさしい緑黄色野菜":
    st.write("内向的でメンタルの強い人。人から注目されることを嫌います。程良い距離感を望んでおり、いつも平和で調和のとれた仲間たちと一緒にいます。")
if option_2 == "C : 甘いもの大好き！お菓子":
    st.write("前向きなエネルギーを発している人。あなたはいつでもどんな時でも最善を尽くし、最高の結果につながるよう努力します。好きな人ができたら、相手を観察し猛烈にアタックすることも。")
if option_2 == "D : 生きる糧！肉！肉！肉！":
    st.write("多くの人から好かれている人です。あなたの自尊心の高さとこれまでの様々な経験が、周囲の人たちを希望と活力で満たします。どんな人の心の内にも入り込み、幅広い人脈を築くでしょう。")


option_3=st.selectbox(
    "Q4. 友達数人とおしゃべりしているとき、自分だけが先日の食事会に呼ばれていなかったことがわかりました。そんなとき、あなたならどうしますか？",
    list(["A：「私も行きたかったなー」と、甘えた声を出す","B：「あー、そうなんだ」と、軽い一言で受け流す","C：「話は変わるけどさ」と、話題をさっと変える","D：「私だけ呼ばれなかったみたいね」と、ぼそっとつぶやく。",])
    )
"あなたが選択したのは、",option_3,"です。"

if option_3 =="A：「私も行きたかったなー」と、甘えた声を出す":
    st.write("A：「私も行きたかったなー」と、甘えた声を出す……八方美人タイプ。笑いながら甘えた声を出しても、腹の底では怒りがこみ上げています。でもあなたは人から嫌われたくない、いつもみんなに愛されていたいと、強く感じている人です。そのため、人前で不快な様子は決して見せないのです。相手が喜ぶなら、心にもないお世辞を言ったり、おべっかを使うことも平気でできます。だれに対してもいい顔をしていたいあなたは、八方美人タイプの腹黒さを持っています。")
if option_3 =="B：「あー、そうなんだ」と、軽い一言で受け流す":
    st.write("B：「あー、そうなんだ」と、軽い一言で受け流す……粘着質タイプ。「何で私を誘ってくれなかったの！」と、文句を言いたいのはやまやま。でもあなたは思ったことをすぐに口走ったり態度に出したりはせず、じっと心に秘めておきます。あとで出席しただれかにこっそり話を聞こう、なぜ自分だけ誘われなかったのか理由を探ろう、などとさまざまな考えをめぐらせているのです。そして自分がされたことをずっと忘れず、いつまでも根に持っている。粘着質タイプの腹黒さがあります。")
if option_3 =="C：「話は変わるけどさ」と、話題をさっと変える":
    st.write("C：「話は変わるけどさ」と、話題をさっと変える。……お子ちゃまタイプ。あなたは自分だけが誘われず、のけ者にされたことが大いに不満でおもしろくないのです。その事実を認めたくありません。みんなが楽しそうに盛り上がっているのも不愉快です。だからこの話はなかったことにしよう、とさりげなく別の話に誘導します。あなたは自分が話題をリードしていないと気がすまないのです。その腹黒さは、いつも自分が中心でないと気がすまない、わがままな子どものようでしょう。")
if option_3 =="D：「私だけ呼ばれなかったみたいね」と、ぼそっとつぶやく。":
    st.write("D：「私だけ呼ばれなかったみたいね」と、ぼそっとつぶやく…リベンジタイプ。本当はキレたいところでしょうが、これでもずいぶん感情を抑えて冷静を装っているのでしょう。なにしろあなたは相当な負けず嫌いですから。自分がのけ者にされた、などと知ったらもう大変。簡単には忘れないし、水に流すなんて無理です。「いつか必ずやり返してやる！」と復讐を固く心に誓い、実行するタイプです。その後もし相手が不幸になれば、小さくガッツポーズもしかねません。")


option_4=st.selectbox(
    "Q5. 恋人とケンカをしたとき、どう振る舞いますか？次の4つから1つを選んでください。",
    list(["相手から謝ってくるまで待つ","別れたくなってくる","すぐに過ちを認める","冷静に考え、自分が悪ければ謝る",])
    )
"あなたが選択したのは、",option_4,"です。"
if option_4 =="相手から謝ってくるまで待つ":
    st.write("あなたは相手から裏切られることを最も恐れています。裏切られて自尊心を傷つけられることが怖いのです。")
if option_4 =="別れたくなってくる":
    st.write("あなたは自分の感情を上手にコントロールできていないようです。そのため相手を疲れさせてしまい、離れていってしまうことも。子供っぽい振る舞いも可愛いものですが、行き過ぎればそれがアダとなってしまうこともあるでしょう。")
if option_4 =="すぐに過ちを認める":
    st.write("あなたは捨てられることに恐怖を感じているようです。いつも相手を優先し、自分をないがしろにしてきました。そのため相手からは軽んじられる傾向にあります。")
if option_4 =="冷静に考え、自分が悪ければ謝る":
    st.write("あなたは誰かに心を開くことがニガテなようです。そのため相手はあなたに不信感を抱くことも。時には素直な気持ちを言葉にするのも良いかもしれませんよ。")

    

img=Image.open("お疲れ様.jpg")
st.image(img,caption="ここで心理テストは終了です！",use_column_width=True)



button = st.button('あなたは……')
if button == True:
    #Yuito
    if option == '乗り物の写真'and option_1=='C : オフホワイト'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='冷静に考え、自分が悪ければ謝る':
        st.write('あなたはおそらくYさんですね？')
        img=Image.open("Yuito.jpg")
        st.image(img,caption="某Yさん",use_column_width=True)
    #Rina
    elif option == 'ペットの写真'and option_1=='A : ラベンダー'and option_2=='B : 体にやさしい緑黄色野菜'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='冷静に考え、自分が悪ければ謝る':
        st.write('あなたはおそらくRさんですね？')
        img=Image.open("Rina.jpg")
        st.image(img,caption="某Rさん",use_column_width=True)
    #Naoshi
    elif option == '大自然の写真'and option_1=='B : ロイヤルブルー'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='冷静に考え、自分が悪ければ謝る':
        st.write('あなたはおそらくNさんですね？')
        img=Image.open("Naoshi.jpg")
        st.image(img,caption="某Nさん",use_column_width=True)
    #Yui
    elif option == 'お料理の写真'and option_1=='C : オフホワイト'and option_2=='C : 甘いもの大好き！お菓子'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='すぐに過ちを認める':
        st.write('あなたはおそらくYさんですね？')
        img=Image.open("Yui.jpg")
        st.image(img,caption="某Yさん",use_column_width=True)
    #Takumi
    elif option == 'お料理の写真'and option_1=='B : ロイヤルブルー'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='冷静に考え、自分が悪ければ謝る':
        st.write('あなたはおそらくTさんですね？')
        img=Image.open("Takumi.jpg")
        st.image(img,caption="某Tさん",use_column_width=True)
    #Ryo
    elif option == 'お料理の写真'and option_1=='B : ロイヤルブルー'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='C：「話は変わるけどさ」と、話題をさっと変える'and option_4=='相手から謝ってくるまで待つ':
        st.write('あなたはおそらくRさんですね？')
        img=Image.open("Ryo.jpg")
        st.image(img,caption="某Rさん",use_column_width=True)
    #Tatsuyoshi
    elif option == '乗り物の写真'and option_1=='D : ランプブラック'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='A：「私も行きたかったなー」と、甘えた声を出す'and option_4=='別れたくなってくる':
        st.write('あなたはおそらくTさんですね？')
        img=Image.open("Tatsuyoshi.jpg")
        st.image(img,caption="某Tさん",use_column_width=True)
    #shin
    elif option == '乗り物の写真'and option_1=='B : ロイヤルブルー'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='相手から謝ってくるまで待つ':
        st.write('あなたはおそらくSさんですね？')
        img=Image.open("Shin.jpg")
        st.image(img,caption="某Sさん",use_column_width=True)
    #Shun
    elif option == '乗り物の写真'and option_1=='D : ランプブラック'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='別れたくなってくる':
        st.write('あなたはおそらくSさんですね？')
        img=Image.open("Shun.jpg")
        st.image(img,caption="某Sさん",use_column_width=True)
    #Tatsuro
    elif option == 'ペットの写真'and option_1=='B : ロイヤルブルー'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='C：「話は変わるけどさ」と、話題をさっと変える'and option_4=='相手から謝ってくるまで待つ':
        st.write('あなたはおそらくTさんですね？')
        img=Image.open("Tatsuro.jpg")
        st.image(img,caption="某Tさん",use_column_width=True)
    #Norika
    elif option == 'ペットの写真'and option_1=='C : オフホワイト'and option_2=='B : 体にやさしい緑黄色野菜'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='別れたくなってくる':
        st.write('あなたはおそらくNさんですね？')
        img=Image.open("Norika.jpg")
        st.image(img,caption="某Nさん",use_column_width=True)
    #Atsuya
    elif option == '大自然の写真'and option_1=='A : ラベンダー'and option_2=='D : 生きる糧！肉！肉！肉！'and option_3=='B：「あー、そうなんだ」と、軽い一言で受け流す'and option_4=='すぐに過ちを認める':
        st.write('あなたはおそらくAさんですね？')
        img=Image.open("Atsuya.jpg")
        st.image(img,caption="某Aさん",use_column_width=True)
    else:
        st.write("すみません、あなたが誰だか分かりませんでした。")
        img=Image.open("アキネーター.jpg")
        st.image(img,caption="",use_column_width=True)
        
        






