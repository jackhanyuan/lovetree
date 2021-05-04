from flask import Flask, render_template, request, redirect


# 配置参数
app = Flask(__name__)
app.debug = True


@app.route('/')
def love():
    return render_template('index.html')


# --host=0.0.0.0 --port=5000    表明任意ip可以访问服务器，端口号为5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=52013, debug=True)
