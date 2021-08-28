from flask import Flask, render_template, url_for, request, redirect
import random

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__, static_folder="img")

contents = [
            '学生時代に最も力を入れた事を教えて下さい。', 
            '自己PRをお願いします。', 
            '現在の就活の軸を教えて下さい。', 
            '当社を志望する理由を教えてください。', 
            '将来のキャリアプランを教えて下さい。',
            '自己紹介をお願いします。',
            '今までで1番の成功体験を教えてください。',
            '今までで1番の挫折を教えてください。',
            '今までで一番うれしかったことは何ですか。',
            '尊敬する人を教えてください。'
            ]


@app.route('/')
def index():
    return render_template('index.html')

# "終了"ボタンを押した場合の処理
@app.route('/revival', methods=['GET', 'POST'])
def revival():
    # GETメソッドの場合
    if request.method == 'GET':
        # トップページにリダイレクト
        return redirect(url_for('index'))
    # POSTメソッドの場合
    else:
        contents.append('学生時代に最も力を入れた事を教えて下さい。')
        contents.append('自己PRをお願いします。')
        contents.append('現在の就活の軸を教えて下さい。')
        contents.append('当社を志望する理由を教えてください。')
        contents.append('将来のキャリアプランを教えて下さい。')
        contents.append('自己紹介をお願いします。')
        contents.append('今までで1番の成功体験を教えてください。')
        contents.append('今までで1番の挫折を教えてください。')
        contents.append('今までで一番うれしかったことは何ですか。')
        contents.append('尊敬する人を教えてください。')
    return render_template('index.html')

# "面接に進む"ボタンを押した場合の処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    # GETメソッドの場合
    if request.method == 'GET':
        # トップページにリダイレクト
        return redirect(url_for('index'))
    # POSTメソッドの場合
    else:
        random.shuffle(contents)
        content = contents[0]
        del contents[0]
        return render_template('questions.html',content=content)

# "次の質問へ"ボタンを押した場合の処理
@app.route('/next', methods=['GET', 'POST'])
def next():
    # GETメソッドの場合
    if request.method == 'GET':
        # トップページにリダイレクト
        return redirect(url_for('index'))
    # POSTメソッドの場合
    else:
        content = contents[0]
        del contents[0]
        contents_length = len(contents)
        return render_template('questions.html',content=content,length=contents_length)

if __name__ == "__main__":
    app.run(debug=True)