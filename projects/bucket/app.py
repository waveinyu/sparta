from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sis7sux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list) + 1

    doc = {
        'num':count,
        'bucket':bucket_receive,
        'done':0
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '등록 완료'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give'] #번호를 숫자로 받아도 ruquest로 넘어올 땐 문자로 받기 때문에 형변환이 필요하다
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({},{'_id':False}))

    return jsonify({'buckets': bucket_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)