__author__ = "yzj"
__data__ = "2020/4/12 15:43"

from crm import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", part=8082, debug=True)







