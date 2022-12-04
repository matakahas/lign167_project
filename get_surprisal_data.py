"""
a script to compute surprisals of sentences in the `surprisal` module
"""
import pandas as pd

import surprisal

def test_surprisal():
    g = surprisal.OpenAIModel(model_id="curie:ft-personal-2022-11-21-16-39-49",
                            openai_api_key="") #API key removed


    stims = [
        "書いたエッセーが権威ある文学賞を受賞したので女性議員は感謝を述べた。",
        "発表した論文が世界中の学者から注目されたので教授は多忙を極めた。",
        "購入した絵画がピカソの作品だったので美術館長は展示会を計画した。",
        "演じた芝居が連日チケットが完売したので役者は海外に招待された。",
        "開発した新製品が今朝社外に発表されたので若手社員は誇りに思った。",
        "デザインしたドレスが大勢の記者に取材されたので女優は自信を付けた。",
        "作った日本酒が先月ガイドブックで特集されたので外国人は周りに認められた。",
        "受けた難病の診断が今朝社内で公表されたので重役は引き継ぎを始めた。",
        "書いたエッセーが権威ある文学賞を受賞した女性議員は感謝を述べた。",
        "発表した論文が世界中の学者から注目された教授は多忙を極めた。",
        "購入した絵画がピカソの作品だった美術館長は展示会を計画した。",
        "演じた芝居が連日チケットが完売した役者は海外に招待された。",
        "開発した新製品が今朝社外に発表された若手社員は誇りに思った。",
        "デザインしたドレスが大勢の記者に取材された女優は自信を付けた。",
        "作った日本酒が先月ガイドブックで特集された外国人は周りに認められた。",
        "受けた難病の診断が今朝社内で公表された重役は引き継ぎを始めた。"
    ]

    surps = g.surprise(stims)
    return surps

if __name__=='__main__':
    surps = test_surprisal()
    df = pd.DataFrame(surps)
    df['cond'] = ['non-island']*8+['island']*8
    df.to_csv('/Users/mahotaka/surprisal/raw_data_ft.csv')
    print('finished computing surprisals of {} sentences'.format(len(df)))